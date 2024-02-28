import React, { useState } from "react";
import MonacoEditor from 'react-monaco-editor';

const Monaco = ({ filetype, code }) => {
  condt [content, setContent] = useState(code);

  const handleEditorChange = (newValue, event) => {
    setContent(newValue);
  }

  return (
    <MonacoEditor
      width="800"
      height="600"
      language={filetype}
      theme="vs-dark"
      value={content}
      onChange={handleEditorChange}
    />
  );
};

export default Monaco;
