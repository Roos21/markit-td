var filtre = []
function onCheckFilter(event){

    if(event.checked){
        filtre.push(event.value)
    }
    else {
        let tmp = filtre
        filtre = []
        for(let index in tmp){
            if(tmp[index] != event.value){
                filtre.push(tmp[index])
            }
        }  
    }

    let csrfTokenValue = document.querySelector('[name=csrfmiddlewaretoken]').value;
    var data = new FormData();
    data.append("filtres",JSON.stringify(filtre)) 
    //data = JSON.stringify(data);
    const request = new Request(
        'filtre',
        {
            method: 'POST',
            body: data,
            headers: {'X-CSRFToken': csrfTokenValue},
        }
    );
    fetch(request).then(response => response.json()).then(result => {
    
        //alert(result["r"]["filtres"]);
        var panel_new = document.getElementById('pro-panel');
        panel_new.innerHTML = result["r"]["filtres"];
    });
    
}

document.getElementById("password").onkeyup = function(){
    let csrfTokenValue = document.querySelector('[name=csrfmiddlewaretoken]').value;
    var data = new FormData();
    data.append("key",document.getElementById("password").value);
    const request = new Request(
        'check_password',
        {
            method: 'POST',
            body: data,
            headers: {'X-CSRFToken': csrfTokenValue},
        }
    );
    fetch(request).then(response => response.json()).then(result => {
        var p = document.getElementById("password");
        if (result["r"]["filtres"]==1) {
            
        } else {
            p.style.border = "1px solid red";
        }
    });
}
