Every drop table has the ability to be restricted with various conditions. This means that only players that meet all the requirements on a drop table will actually access it when performing an action. Here is a list of available conditions.

### Conditions tables (Since 1.9.5)

You can create condition tables in `conditions.yml`. You will then be able to reference an entire set of conditions at once using the `from` condition.

```yml
#Example
test-condition:
  - 'level{amount=10}'
  #Will load the 2 conditions from test-condition-2.
  - 'from{source=test-condition-2}'

test-condition-2:
  - 'world{name=world}'
  - 'level{profession=mining;amount=3}'
```

## All the conditions
| Condition | Format |
|-----------|--------|
| From | `from{source=condition-id}` |
| Main Level | `level{amount=LEVEL_HERE}` |
| Profession Level | `level{profession=PROFESSION_NAME;amount=LEVEL_HERE}` |
| Current Biome | `biome{name=BIOMES}` |
| Current World | `world{name=WORLD_NAME}` |
| Permission | `permission{node=PERMISSION_NODE}` |

```
```