//Pause makes counter blink, Resume to remove
(function ($) {
    "use strict";

    /*global window */

    var l4f = {
        init: function () {

            var csfrtoken = $("[name='csrfmiddlewaretoken']").val(),
                message;
            $(".arrow-up").on("click", function () {
                var num = Number($("#id_number_of_players").val());
                if (num < 3) {
                    $("#id_number_of_players").val((num + 1).toString());
                }
            });

            $(".arrow-down").on("click", function () {
                var num = Number($("#id_number_of_players").val());
                if (num > 1) {
                    $("#id_number_of_players").val((num - 1).toString());
                }
            })

            var callhistory = setInterval(function () {
                $.ajax({
                    url: "history/",
                    dataType: "json",
                    data: {"csrfmiddlewaretoken": csfrtoken},
                    method: "POST",
                    success: function (data) {
                        $(".slack-messages").html("");
                        $.each(data.messages, function(i,val) {
                            message = data.messages[i].username + ": " +
                                data.messages[i].text + "<br>";
                            $(".slack-messages").append(message);
                        })
                    }
                })
            }, 5000);
        }

    };

    l4f.init();
}(window.jQuery));
