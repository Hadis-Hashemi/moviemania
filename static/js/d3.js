console.log(d3)
var tbody = d3.select("tbody")
d3.json("/api/v1.0/imdb_data", function(error, response){
    console.log(response)
    var imdbData = response.slice(0,10);

    imdbData.forEach(function(imdb) {
        console.log(imdb);
        // Append each row with the data
        var row = tbody.append("tr");

        Object.entries(imdb).forEach(function([key, value]) {
            console.log(key, value);
            // Append each value to the corresponding cell
            var cell = row.append("td");
            cell.text(value);
        });
    });
});
var button = d3.select("#filter-btn");
button.on("click", function() {
    tbody.html("");

    var inputElement = d3.select("#datetime");
    // Get the value property of the input date, state, shape
    var inputValue = inputElement.property("value");
    console.log(inputValue);


//     filteredData.forEach(function(selections) {

//     console.log(selections);
//     // Append one table row 
//     var row = tbody.append("tr");
//     // Use `Object.entries` to print each UFO Sighting value
//     Object.entries(selections).forEach(function([key, value]) {
//         console.log(key, value);
//         var cell = row.append("td");
//         cell.text(value);
//     });
// });
});