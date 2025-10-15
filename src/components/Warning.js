export default function Warning({title='Warning', children}) {
  return (
    <div className="big-tip">
      <div className="tip-icon">⚠️</div>
      <div className="tip-body">
        {children}
      </div>
    </div>
  );
}
