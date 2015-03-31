// ==UserScript==
// @name         My Fancy New Userscript
// @namespace    http://your.homepage/
// @version      0.1
// @description  enter something useful
// @author       You
// @match        http://www.nicovideo.jp/watch/*
// @grant        nones
// ==/UserScript==

// Constants
DOWN_API_URL = "http://flapi.nicovideo.jp/api/getflv/";
EQUAL_STR = "=";

// Get API URL
current_urls = document.URL.split("/");
url_last = current_urls[current_urls.length-1];

api_url = DOWN_API_URL + url_last;

response_data = "undefined";

// Access to API
req = new XMLHttpRequest;
req.open("GET", api_url, false);
req.withCredentials = true;
req.send(null);

response_data = req.responseText;

// Get Data from API
query_regex = /([^&]+)=([^&]*)/g
query_map = {};

query_data = response_data.match(query_regex);

for (i=0; i < query_data.length; i++) {
    splitted = query_data[i].split(EQUAL_STR);
    query_map[splitted[0]] = decodeURIComponent(splitted[1]);
}

// Create Anchor Tag
download_url = query_map["url"];
a_tag = document.createElement('a');
a_tag.innerText = download_url;
a_tag.setAttribute("href", download_url);

// Append  Anchor Tag to #videoHeaderDetail
videodetail_tag = document.getElementById("videoHeaderDetail");
videodetail_tag.appendChild(a_tag);
