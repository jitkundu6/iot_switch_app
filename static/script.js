function sendMessage() {
    const message = $('#message').val();
    $.ajax({
        url: '/send_message',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ message: message }),
        success: function(response) {
            $('#send_status').text(response.status);
        },
        error: function() {
            $('#send_status').text('Failed to send message');
        }
    });
}

function readMessage() {
    $.ajax({
        url: '/read_message',
        type: 'GET',
        success: function(response) {
            $('#latest_message').text('Latest message: ' + response.message);
        },
        error: function() {
            $('#latest_message').text('Failed to read message');
        }
    });
}

function controlSwitch(status) {
    $.ajax({
        url: '/control_switch',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ status: status }),
        success: function(response) {
            $('#switch_status').text(response.status);
        },
        error: function() {
            $('#switch_status').text('Failed to control switch');
        }
    });
}
