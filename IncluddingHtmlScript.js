(function() {
    var z, i, elmnt, file, xhttp;
    
    z = document.getElementsByTagName("*");
    for (i = 0; i < z.length; i++) {
      elmnt = z[i];
    
      file = elmnt.getAttribute("w3-include-html");
      if (file) {
        
        xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
          if (this.readyState == 4) {
            if (this.status == 200) {elmnt.innerHTML = this.responseText;}
            if (this.status == 404) {elmnt.innerHTML = "Page not found.";}
            
            elmnt.removeAttribute("include-html");
            includeHTML();
          }
        }      
        xhttp.open("GET", file, true);
        xhttp.send();
        return;
      }
    }
}())

//Как это использовать?
/*

//Примеры
<div include-html="content.html"></div>

1.<div></div> // можно любой атрибут начиная от <h1> заканчивая любым дргуим
2.обязательное метод include-html
3. = "сылка на файл котоырй находиться в этом каталоге" если файл находитсья в другой папке нужно указывать путь так
        // "folder/test.html"


*/
