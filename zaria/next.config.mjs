// next.config.js
import MonacoWebpackPlugin from 'monaco-editor-webpack-plugin';

export default {
  webpack: (config, { isServer }) => {
    // Add MonacoWebpackPlugin to the webpack configuration
    config.plugins.push(
      new MonacoWebpackPlugin({
        // Specify the languages you want to include
        // Example: ['json', 'typescript', 'javascript', 'html', 'css']
        languages: ['json', "javascript"]
      })
    );

    // Return the modified configuration
    return config;
  },
};
