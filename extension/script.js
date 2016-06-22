/* Script inserted to web page */
var shortUrlDomain = ['http://bit.ly/', 'http://goo.gl/', 'https://goo.gl/', 'http://ppt.cc/', 'http://0rz.tw/', 'http://tinyurl.com/', 'https://4fun.tw/', 'http://mcaf.ee/', 'http://baidu.nu/', 'http://t.cn/']

window.addEventListener("mouseover", function(event)
{
    var link = event.target;
    while (link && link.localName != "a"){
      link = link.parentNode;
    }

    if (link && isShort(link.href)) {
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
    tooltip.innerHTML = '<iframe src="https://140.112.30.32:4443/analyze?url=' + link.href + '" style="background-color:white;" width="380" height="420"/>';
    link.appendChild(tooltip);
}

function isShort(url){
    for (var i = 0; i < 9; i++){
        if (url.indexOf(shortUrlDomain[i]) > -1)
            return true;
    }
    return false;
}