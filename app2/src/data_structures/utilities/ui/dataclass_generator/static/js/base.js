/**
 * Sets text in a modal message and shows it in UI.
 * @param {string} modal_title
 * @param {string} modal_body
 * @param {boolean} enable_close
 * @param {boolean} enable_timeout
 */
function setModalMessage(modal_title, modal_body, enable_close = true, enable_timeout = false) {
    let modal = $('#modal');
    modal.find('.modal-title').text(modal_title);
    modal.find('.modal-body').text(modal_body);

    if (!enable_close) {
        modal.prop('data-backdrop', 'static');
        modal.prop('data-keyboard', false);
        modal.find('.modal-footer').prop('style', 'display: none;');
    } else {
        modal.removeProp('data-backdrop');
        modal.removeProp('data-keyboard');
        modal.find('.modal-footer').removeProp('style');
    }

    if (enable_timeout) {
        modal.on('show.bs.modal', function () {
            let authModal = $(this);
            clearTimeout(authModal.data('hideInteval'))
            authModal.data('hideInterval', setTimeout(function () { authModal.modal('hide'); }, 6000));
        });
    }
    modal.modal('show');
}

/**
 * Sets a failure modal message.
 * @param {string} failed_message
 */
function failedModalMessage(failed_message) {
    let message = "There was an error while performing this process. Reason -> " + failed_message;
    setModalMessage("Failed to performs process", message)
}

function buttonClickedLoading(button) {
    button.html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>');
    button.prop('disabled', true);
}

/**
 * Performs a request to a given URL.
 * @param {string} url
 * @param {string} method
 * @param {Object} data
 * @returns {Promise<Response>} response
 */
async function request(url, method = 'GET', data = {}) {
    return await fetch(url, {
        method: method,
        cache: 'no-cache',
        credentials: 'same-origin',
        body: JSON.stringify(data)
    });
}

/**
 * Performs an authenticated request.
 * If it fails, it will show a modal message and renew the access token.
 * @param {string} url
 * @param {string} method
 * @param {Object} data
 * @returns {Promise<Object>} response
 */
function authenticatedRequest(url, method = 'GET', data = {}) {
    return request(url, method, data).then(async (response) => {
        return await response.blob();
    }).catch((error) => {
        if (error.message === "Failed to fetch") {
            let modal_body = 'Authenticate token has been expired. Reloading page to get renew access...'
            setModalMessage('Authentication Timeout', modal_body, false, true)

            $('#modal').on('hide.bs.modal', function () { window.location.reload(); });
        } else {
            failedModalMessage(error.message);
        }
    });
}

/**
 * Executes an authenticated Ajax request for a given URL and method.
 * This function handles the auth token timeout.
 * @param {string} url
 * @param {string} method
 * @param {Object} data
 * @returns {*} response
 */
function authenticatedAjaxRequest(url, method = 'GET', data = {}) {
    return $.ajax({
        url: url,
        method: method,
        data: JSON.stringify(data),
        credentials: 'same-origin'
    }).done((response) => {
        return response;
    }).catch((error) => {
        if (error.status === 0) {
            let modal_body = 'Authenticate token has been expired. Reloading page to get renew access...'
            setModalMessage('Authentication Timeout', modal_body, false, true)

            $('#modal').on('hide.bs.modal', function () { window.location.reload(); });
        } else {
            failedModalMessage(error.responseJSON.message);
            throw Error(error.statusText);
        }
    });
}

/**
 * Copies to clipboard the content of output box with commonly has the data contract.
 */
function copyToClipboard(label) {

    // If textToCopy is not provided, use a default value or an empty string
    label = label || 'Data Contract';
    let outputBox;
    // Select the text to be copied
    if (label === 'Synthetic Data') {
        outputBox = document.getElementById('synthetic-data-output-box');
    }
    else {
        outputBox = document.getElementById('output-box');
    }
    outputBox.select();
    outputBox.setSelectionRange(0, 99999); // For mobile devices

    // Copy the text inside the text field
    navigator.clipboard.writeText(outputBox.value).then(function (x) {
        // Alert the copied text
        blurt('Success', `${label} copied to clipboard.`, 'success');
    });
}
