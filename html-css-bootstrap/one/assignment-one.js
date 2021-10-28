function increase(id){
    var x = document.getElementById(id).innerHTML ; 
    var val = parseInt(x);
    val++;
    document.getElementById(id).innerHTML = val ;
}

function decrease(id){
    var x = document.getElementById(id).innerHTML;
    var val = parseInt(x);
    if(val==0){
        document.getElementById(id).innerHTML = val ;
    }
    else{
        val--;
        document.getElementById(id).innerHTML = val ;
    }
    
}