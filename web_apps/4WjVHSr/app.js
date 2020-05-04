
function update() {
    
    /* Getting all the input into an object that we will pass to the backend as a parameter of the call*/
    variables = {};
    
    $('.form-control').each(function(index){
        variables[$(this).prop('id')] = $(this).val();
    });
    
    
    console.log("sending to backend : ", variables);
    
    var flow_run =$.getJSON(getWebAppBackendUrl('update')+'/'+JSON.stringify(variables),function(data){
        console.log(data);
        
        /*Refresh the dashboard page*/
        window.top.location.reload();
     }) 
 }

d3.select("#update").on("click", update);