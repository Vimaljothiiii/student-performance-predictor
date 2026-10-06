function predict() {

    let study_hours = document.getElementById("study_hours").value;
    let attendance = document.getElementById("attendance").value;
    let previous_score = document.getElementById("previous_score").value;
    let assignment_score = document.getElementById("assignment_score").value;

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            study_hours: Number(study_hours),
            attendance: Number(attendance),
            previous_score: Number(previous_score),
            assignment_score: Number(assignment_score)
        })
    })

    .then(response => response.json())

    .then(data => {

        document.getElementById("result").innerHTML =
            "Result: " + data.prediction;

    })

    .catch(error => {

        document.getElementById("result").innerHTML =
            "Error connecting to server";

        console.log(error);

    });
}