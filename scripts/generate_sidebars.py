import os
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

def _read_md_lines(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().split('\n')
    except Exception:
        return []

@dataclass
class MarkdownMeta:
    """Métadonnées extraites d'un fichier Markdown."""
    title: str
    order: Optional[int]
    collapsible: Optional[bool] = None

def parse_markdown_metadata(file_path: str) -> MarkdownMeta:
    """
    Lit un fichier Markdown et retourne ses métadonnées principales
    sous forme d'une instance de MarkdownMeta.

    Métadonnées prises en charge:
    - title: depuis le frontmatter `title` ou le premier heading `#`;
             sinon, le nom du fichier.
    - order: depuis le frontmatter `order` (int). Si absent ou invalide, None.
    """
    lines = _read_md_lines(file_path)

    title: Optional[str] = None
    order_val: Optional[int] = None
    collapsible_val: Optional[bool] = None

    # Frontmatter YAML très simplifié
    if lines and lines[0].strip() == '---':
        for line in lines[1:]:
            if line.strip() == '---':
                break
            l = line.strip()
            if l.startswith('title:') and title is None:
                title = l.split(':', 1)[1].strip().strip('"').strip("'")
            elif l.startswith('order:') and order_val is None:
                raw = l.split(':', 1)[1].strip()
                try:
                    order_val = int(raw)
                except Exception:
                    try:
                        order_val = int(float(raw))
                    except Exception:
                        order_val = None
            elif l.startswith('collapsible:') and collapsible_val is None:
                rawb = l.split(':', 1)[1].strip().lower()
                if rawb in ('true', 'yes', 'on'):
                    collapsible_val = True
                elif rawb in ('false', 'no', 'off'):
                    collapsible_val = False

    # Si pas de title via frontmatter, chercher premier heading
    if not title:
        for line in lines:
            if line.startswith('# '):
                title = line.replace('# ', '').strip()
                break

    if not title:
        title = Path(file_path).stem.replace('-', ' ').replace('_', ' ').title()

    return MarkdownMeta(title=title, order=order_val, collapsible=collapsible_val)

def collect_link_data(folder_path: str, base_path: str, include_index: bool) -> list:
    """
    Collecte les liens (fichiers .md) d'un dossier sous forme de données triables,
    avec support optionnel pour inclure `index.md`.
    Retourne une liste d'objets: {type:'link', text, link, _order}
    """
    items = []
    for f in sorted(os.listdir(folder_path)):
        f_path = os.path.join(folder_path, f)
        if not (os.path.isfile(f_path) and f.endswith('.md')):
            continue
        if not include_index and f == 'index.md':
            continue
        md = parse_markdown_metadata(f_path)
        link = base_path if f == 'index.md' else base_path + f.replace('.md', '')
        items.append({
            'type': 'link',
            'text': md.title,
            'link': link,
            '_order': md.order if md.order is not None else 9999
        })
    return items

def generate_sidebar_for_folder(folder_path, base_path):
    """
    Génère une sidebar pour un dossier donné.
    
    Args:
        folder_path: Chemin absolu du dossier à scanner
        base_path: Chemin de base pour les liens (ex: '/mythiclib/')
    
    Returns:
        Liste de sections de sidebar
    """
    sections = []
    
    # Lister tous les éléments dans le dossier
    items = sorted(os.listdir(folder_path))
    
    # Séparer les fichiers et les dossiers
    files = []
    folders = []
    
    for item in items:
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path) and item.endswith('.md'):
            files.append(item)
        elif os.path.isdir(item_path) and item != 'uploads':
            folders.append(item)
    
    # Ajouter les fichiers à la racine (si présents) triés par `order`
    if files:
        root_items_data = collect_link_data(folder_path, base_path, include_index=True)
        if root_items_data:
            # Trier par order puis par titre
            root_items_data.sort(key=lambda x: (x['_order'], x['text']))
            root_items = [{'text': x['text'], 'link': x['link']} for x in root_items_data]
            # Garder la section racine en tête
            sections.append({
                'text': 'Getting Started',
                'items': root_items,
                '_order': -1
            })
    
    # Générer récursivement chaque sous-dossier comme une catégorie potentiellement imbriquée
    for folder in folders:
        folder_path_full = os.path.join(folder_path, folder)

        def generate_category_section(current_folder_path: str, current_base_path: str) -> dict:
            # Déterminer le titre et l'ordre de la catégorie via index.md si présent
            index_path = os.path.join(current_folder_path, 'index.md')
            if os.path.exists(index_path):
                md_index = parse_markdown_metadata(index_path)
                category_title = md_index.title
                category_order = md_index.order if md_index.order is not None else 9999
                category_collapsed = True if md_index.collapsible is True else None
            else:
                # Fallback sans index.md
                category_title = os.path.basename(current_folder_path).replace('-', ' ').replace('_', ' ').title()
                category_order = 9999
                category_collapsed = None

            # Collecter les liens (fichiers .md hors index.md)
            links_data = collect_link_data(current_folder_path, current_base_path, include_index=False)

            # Collecter les sous-catégories imbriquées
            sections_data = []
            for sub in sorted(os.listdir(current_folder_path)):
                sub_path = os.path.join(current_folder_path, sub)
                if os.path.isdir(sub_path) and sub != 'uploads':
                    sub_section = generate_category_section(sub_path, f"{current_base_path}{sub}/")
                    sections_data.append({
                        'type': 'section',
                        'text': sub_section['text'],
                        'items': sub_section['items'],
                        '_order': sub_section.get('_order', 9999),
                        'collapsed': sub_section.get('collapsed')
                    })

            # Fusionner liens et sous-sections et trier par `order` puis `text`
            merged_items = links_data + sections_data
            merged_items.sort(key=lambda x: (x.get('_order', 9999), x['text']))

            # Nettoyer les champs internes
            final_items = []
            for it in merged_items:
                if it['type'] == 'link':
                    final_items.append({'text': it['text'], 'link': it['link']})
                else:
                    section_obj = {'text': it['text'], 'items': it['items']}
                    if it.get('collapsed') is True:
                        section_obj['collapsed'] = True
                    final_items.append(section_obj)

            section_result = {
                'text': category_title,
                'items': final_items,
                '_order': category_order
            }
            if category_collapsed is True:
                section_result['collapsed'] = True
            return section_result

        top_section = generate_category_section(folder_path_full, f"{base_path}{folder}/")
        sections.append(top_section)
    
    # Trier les sections par order puis titre, et produire la sidebar finale
    sections.sort(key=lambda s: (s.get('_order', 9999), s['text']))
    sidebar = []
    for s in sections:
        entry = {'text': s['text'], 'items': s['items']}
        if s.get('collapsed') is True:
            entry['collapsed'] = True
        sidebar.append(entry)
    return sidebar

def generate_sidebar_js(output_path: str, sidebars_config: dict):
    """
    Génère le fichier sidebar.js avec les configurations fournies.
    
    Args:
        output_path: Chemin du fichier de sortie
        sidebars_config: Dictionnaire des configurations de sidebar
    """
    js_content = "export const generatedSidebars = "
    js_content += json.dumps(sidebars_config, indent=2, ensure_ascii=False)
    js_content += ";\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_content)

FOLDERS_GENERATED = ['mythiclib', 'mmoitems', 'mmocore', 'mmoinventory', 'mmoprofiles',
                     'bounty-hunters', 'contracts']

if __name__ == "__main__":
    project_root = Path(__file__).parent.parent
    output_file = project_root / ".vitepress" / "sidebars.js"

    # Generate all sidebars
    sidebars_config = {}
    for folder_name in FOLDERS_GENERATED:
        sidebars_config[f'/{folder_name}/'] = generate_sidebar_for_folder(
            str(project_root / folder_name),
            f'/{folder_name}/'
        )
        print(f"✓ Generated sidebar: {folder_name}")
    
    # Generate sidebars.js file
    generate_sidebar_js(str(output_file), sidebars_config)
    
    print("All sidebars were generated")
