function sendDataToServer(data){
    fetch('http://localhost:5000/track.json', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    })
}

let startTime = null;
let tracking = false;

function checkCurrentTab() {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (!tabs || tabs.length === 0) return;
    const tab = tabs[0];
    const url = tab.url || "";

    if (url.includes("youtube.com/watch") || url.includes("youtube.com/shorts")) {
      if (!tracking) {
        startTime = new Date();
        tracking = true;
      }
    } else {
      if (tracking) {
        const endTime = new Date();
        const duration = Math.floor((endTime - startTime) / 1000);
        tracking = false;
        sendDataToServer({
            duration: duration,
            startTime: startTime,
            endTime: endTime
        })
        startTime = null;
      }
    }
  });
}


setInterval(() => {
    checkCurrentTab();
}, 10000);

// Trigger check when tab changes
chrome.tabs.onActivated.addListener(checkCurrentTab);

// Trigger check when tab content loads
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === "complete") {
    checkCurrentTab();
  }
});

// Trigger check when user switches windows
chrome.windows.onFocusChanged.addListener((windowId) => {
  if (windowId === chrome.windows.WINDOW_ID_NONE) return;
  checkCurrentTab();
});
