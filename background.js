// Listen for messages from content script
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'videoInfo') {
      // Received video information from content script
      const videoInfo = request.data;
      
      // Log the video information (you can implement your logic here)
      console.log('Received video info:', videoInfo);
    }
  });
  