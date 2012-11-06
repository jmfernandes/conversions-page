function toggle(id){
    ul = "ul_" + id;
    img = "img_" + id;
    ulElement = document.getElementById(ul);
    imgElement = document.getElementById(img);
    if (ulElement){
            if (ulElement.className == 'closed'){
                    ulElement.className = "open";
                    imgElement.src = "opened.gif";
                    }else{
                    ulElement.className = "closed";
                    imgElement.src = "closed.gif";
                    }
            }
    }
