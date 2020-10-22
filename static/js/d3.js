console.log(d3)
var tbody = d3.select("tbody")
d3.json("/api/v1.0/imdb_data", { method: "GET" })
    .then(function (response) {
        // console.log(response)
        var imdbData = response.slice(0, 10);

        imdbData.forEach(function (imdb) {
            console.log(imdb);
            // Append each row with the data
            var row = tbody.append("tr");

            Object.entries(imdb).forEach(function ([key, value]) {
                console.log(key, value);
                // Append each value to the corresponding cell
                var cell = row.append("td");
                cell.text(value);
            });
        });
    });
var button = d3.select("#filter-btn");
button.on("click", function () {
    tbody.html("");

    var inputElement = d3.select("#datetime");
    // Get the value property of the input date, state, shape
    var inputValue = inputElement.property("value");
    console.log(inputValue);
    d3.json("/api/v1.0/flickerpicker", {
        method: "POST",
        body: JSON.stringify({ inputValue }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(function (response) {
        console.log(response);
        message = "You may like these movies ";
        if (response[0] != null) {
            message = message + response[0]
        }
        alert(message)
        var flickerData = response
    }).catch(function (error) { console.log(error) });


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

function openCity(evt, cityName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}


// window.onload=function(){
//     document.getElementById("choose").click();
//   };