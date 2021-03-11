function download(){
    var http = new XMLHttpRequest();
    var url = '/';
    var uri = document.getElementById("input").value; 
    var params = 'uri='+uri;
    http.open('POST', url, true);
    http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            document.getElementById("download-div").innerHTML = http.responseText;
        }
        
    } 
    http.send(params);
}
