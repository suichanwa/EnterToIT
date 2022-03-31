function ajaxload(){
    var xhr=new XMLHttpRequest();
    xhr.onreadystatechange=function(){
        if(this.readyState==4){
            if(this.status >=200 && xhr.status < 300){
                document.getElementById('news').innerHTML=this.responseText;
            }
        }
    }
    xhr.open('GET', 'ajax.php');
    xhr.send();
}