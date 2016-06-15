/* Script inserted to web page */
window.addEventListener("mouseover", function(event)
{
    var link = event.target;
    while (link && link.localName != "a"){
      link = link.parentNode;
    }
    if (link) {
    	console.log(link.href)
    	res = httpGet(link.href)	// no response
    	console.log(res)
    }
}, false);

/* Doesn't Work */
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl); // false for synchronous request
    xmlHttp.send();
    return xmlHttp.responseText;
}
