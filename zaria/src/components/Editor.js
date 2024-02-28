import React, { useEffect, useState } from "react";
import Editor from '@monaco-editor/react';
// Editor.js
const EditorPage = ({ content,filetype, handlechange }) => {
  return (
    <div className="w-4/5 bg-gray-800 text-gray-100">
      <div className="p-4 pl-8 font-bold text-2xl">Code Editor</div>
      <div className="pl-8">
        <Editor height="85vh" language={filetype} theme="vs-dark" value={content} onChange={handlechange}/>
      </div>
    </div>
  );
};

export default EditorPage;

