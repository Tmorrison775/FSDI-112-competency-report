












function postCODE() {
    $.ajax({
        url: '/api/genres',
        type: "POST",
        contentType: 'application/json',
        data: JSON.stringify(newG),
        success: function (res) {
            console.log(res);
        },
        error: function (details) {
            console.log("Error on POST request: ", details);
        }
    })
}






function displayMovie(movie){
    console.log("this works");
    var container = $(".cat-container");
    var li= `
    <div class="card" style="width: 18rem;">
  <img src="${movie.image}" class="card-img-top" alt="Movie Image">
  <div class="card-body bg-light">
    <h5 class="card-title">${movie.title}</h5>
    <p class="card-text">
    Genre: ${movie.genre}<br>
    Release Year: ${movie.release_year}<br>
    Duration: ${movie.duration_min}<br>
    Price: ${movie.price}<br>
    In Stock: ${movie.in_stock}<br>
    
    
    </p>
    <a href="#" class="btn btn-primary">Rent</a>
  </div>
</div>`
 
    container.append(li);
}






function getData(){
    $.ajax({
        url:'/api/movies',
        type: "GET",
        success: function(res){
            var movies = res.objects;
            for(var i = 0; i<movies.length;i++){
                displayMovie(movies[i]);
            }

        },
        error: function(res){
            console.log("Error on get request: ", res);
        }
    });
}





function init(){
    console.log("Hello catalog page");
    getData();
}

window.onload = init();
