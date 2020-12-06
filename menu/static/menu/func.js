document.addEventListener('DOMContentLoaded',()=>{
    var expanded = false;
    document.querySelector('.selectbox').onclick = () =>
     {
        var checkboxes = document.getElementById("checkboxes");
        if (!expanded) {
            checkboxes.style.display = "block";
            expanded = true;
        } else {
            checkboxes.style.display = "none";
            expanded = false;
        }
    }
  });