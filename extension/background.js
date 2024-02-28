// background.js

// Keep track of injected scripts for each tab
const injectedScripts = {};

chrome.webNavigation.onDOMContentLoaded.addListener((details) => {
    const tabId = details.tabId;

    // Check if the script has already been injected for this tab
    if (!injectedScripts[tabId]) {
        chrome.scripting.executeScript({
            target: {tabId: tabId},
            files: ['foreground.js'],
        });
        
        // Set the flag to indicate that the script has been injected for this tab
        injectedScripts[tabId] = true;
    }
}, {url: [{schemes: ['http', 'https']}]}); 

// Reset the flag when the page is updated (e.g., reloaded)
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete') {
        // Reset the flag indicating that the script has been injected for this tab
        injectedScripts[tabId] = false;
    }
});
