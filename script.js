/* Script inserted to web page */
window.addEventListener("mouseover", function(event)
{
    var link = event.target;
    while (link && link.localName != "a"){
      link = link.parentNode;
    }
    if (link) {
    	console.log(link.href);
    	res = httpGet(link.href);	// no response
    	console.log(res);
        show(link);
    }
}, false);

document.body.onmouseout = function(e){
    var tooltipNode = e.target.querySelector('.tooltip');

    if (!tooltipNode) {
        return;
    }
    tooltipNode.parentElement.removeChild(tooltipNode);
}

function show(link)
{
    var tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.innerHTML = '<div class="tooltip-loader">HELLO</div>';

    link.appendChild(tooltip);
}

/* Doesn't Work */
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl); // false for synchronous request
    xmlHttp.send();
    return xmlHttp.responseText;
}