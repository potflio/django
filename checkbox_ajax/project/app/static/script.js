$(document).ready(function () {
    $("#create").on('click', function () {
        $name = $('#name').val();
        $skills = $("input[name='skills']:checked").val();
        $hobbies = []
        $('input[name="hobbies"]:checked').each(function () {
            $hobbies.push($(this).val());
        });
        if ($name == "" || $skills == "" || $hobbies == "") {
            alert("fill the form")
        } else {
            $.ajax({
                url: 'submit',
                type: 'POST',
                data: {
                    name: $name,
                    skills: $skills,
                    hobbies: JSON.stringify($hobbies),
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function (response) {
                    alert("successfully")
                    window.location = "/"
                },
                error:function(response){
                    alert("warning")
                }
            })
        }
    });
});