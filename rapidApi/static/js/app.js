//search for tiles, find streaming sources
$(document).ready(() => {
  $('#searchForm').on('submit', (e) => {
    let searchText = $('#searchText').val();
    showSearch(searchText);
    e.preventDefault();
  });
});


function showSearch(searchText){
  console.log(searchText);
  function streamResults(){
      $.ajax({
        "asynch": true,
        "crossDomain": true,
        "url": "https://rapidapi.p.rapidapi.com/lookup?term="+searchText+"&country=us",
        "method": 'GET',
        "headers": {
          "x-rapidapi-host": "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com",
          "x-rapidapi-key": "86d2d8e2fdmsh34190cd508ea626p114b8ajsn678b41441545"
          },
          dataType: 'json',
          success: function(data) {
              console.log(data);
              var y = 0;
              let output = '';
              for (var x = 0; x < data.results.length; x++) {
                  console.log(x);
                  console.log(data.results[x]);
                  var showName = data.results[x].name;
                  var showImage = data.results[x].picture;

                  output += `
                  <div class="card">
                    <img class="card-img-top" src="${showImage}" alt="Card image">
                    <div class="card-body">
                      <h4 class="card-title">${showName}</h4>
                  `;
                  for (var i = 0; i < data.results[x].locations.length; i++) {
                    var location = data.results[x].locations[i].display_name
                    var locationUrl = data.results[x].locations[i].url
                    var locationIcon = data.results[x].locations[i].icon
                    if (location == "iTunes") {
                      console.log("ITUNES");
                      console.log(locationUrl);
                      output += `
                      <br>
                      `;
                      output += `
                      <a href="${locationUrl}" class="btn btn-primary"><img src="${locationIcon}" alt="Watch on Itunes" style="max-height:30px;"></a>
                      `;
                    }
                    if (location == "Netflix") {
                      console.log("NETFLIX");
                      //netflixLink created in response to special treatment required by netflix 
                      console.log(locationUrl.substring(7));
                      var netflixLink = locationUrl.substring(7);
                      output += `
                      <br>
                      `;
                      output += `
                      <a href="https://${netflixLink}" class="btn btn-primary"><img src="${locationIcon}" alt="Watch on Netflix" style="max-height:30px;"></a>
                      `;
                      //API link goes wonky without the https
                    }
                    if (location == "Amazon Instant") {
                      console.log("AMAZON INSTANT");
                      console.log(locationUrl);
                      output += `
                      <br>
                      `;
                      output += `
                      <a href="${locationUrl}" class="btn btn-primary"><img src="${locationIcon}" alt="Watch on Amazon Instant" style="max-height:30px;"></a>
                      `;
                    }
                    if (location == "Amazon Prime") {
                      console.log("AMAZON PRIME");
                      console.log(locationUrl);
                      output += `
                      <br>
                      `;
                      output += `
                      <a href="${locationUrl}" class="btn btn-primary"><img src="${locationIcon}" alt="Watch on Amazon Prime" style="max-height:30px;"></a>
                      `;
                    }
                    if (location == "Google Play") {
                      console.log("Google Play");
                      console.log(locationUrl);
                      output += `
                      <br>
                      `;
                      output += `
                      <a href="${locationUrl}" class="btn btn-primary"><img src="${locationIcon}" alt="Watch on Google Play" style="max-height:30px;"></a>
                      `;
                    }
                    if (location == "Hulu") {
                      console.log("Hulu");
                      console.log(locationUrl);
                      output += `
                      <br>
                      `;
                      output += `
                      <a href="${locationUrl}" class="btn btn-primary"><img src="${locationIcon}" alt="Watch on Hulu" style="max-height:30px;"></a>
                      `;
                    }

                  }

                  //ENDS the output, so all the </div> n such.
                  //example the </h1>
                  output += `
                  </div>
                </div>
                  `;

              }

              $('#movies').html(output);





          }
      });
  }

      $('#btn').click(function(e) {
        e.preventDefault();
         streamResults();


  });
    streamResults();

}
