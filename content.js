// Find the element containing the video title
const videoTitleElement = document.querySelector('h1.title');

// Extract the video title
const videoTitle = videoTitleElement ? videoTitleElement.textContent.trim() : '';

// Find the element containing the video ID
const videoIdElement = document.querySelector('meta[itemprop="videoId"]');

// Extract the video ID
const videoId = videoIdElement ? videoIdElement.getAttribute('content') : '';

// Find the element containing the channel name
const channelNameElement = document.querySelector('.ytd-channel-name a');

// Extract the channel name
const channelName = channelNameElement ? channelNameElement.textContent.trim() : '';

// Create an object with the extracted information
const videoInfo = {
  title: videoTitle,
  id: videoId,
  channel: channelName
};

// Send the video information to the background script
chrome.runtime.sendMessage({ action: 'videoInfo', data: videoInfo });
