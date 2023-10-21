const Template = ({
    source,
    header,
    body
}) => `
<div class="accordion-item">
    <h2 class="accordion-header">
        <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#${source}_${header}"
            aria-controls="work_table">
            Table name: ${header}
        </button>
        <button class="btn btn-save btn-success" onclick="saveDataContract(this);">Save Data Contract</button>
    </h2>
    <div id="${source}_${header}" class="accordion-collapse collapse" aria-labelledby="headingOne">
        <div class="accordion-body">
            <div class="form-floating">
                <textarea class="form-control data-contract" placeholder="Data Contract"
                    style="height: 500px">${body}</textarea>
                <label for="output-box">Data Contract</label>
            </div>
        </div>
    </div>
</div>
`

/**
 * Transform an array of dictionaries that contains name and value to a dictionary.
 * If array contains tables list value, it will create a list of values.
 * @param {Array} formArray Interface form array values.
 * @returns {Object} Body dictionary.
 */
function getFormDataAsDict(formArray) {
    let body = {}
    let tables = []
    $.each(formArray, function () {
        if (this.name === 'table-name' && !this.value) {
            return;
        }

        if (this.name === 'tables-list' && this.value) {
            tables.push(this.value);
            return;
        }

        body[this.name] = this.value;
    });

    if (tables.length) {
        body['tables-list'] = tables
    }

    return body
}

/**
 * Function will auto download to the client a file given a content and a file name.
 * @param {string} blob_data Blob object data.
 * @param {string} mime_type Mime type value for download file.
 * @param {string} file_name File name.
 */
function downloadBlobFile(blob_data, mime_type, file_name) {
    let text = new Blob([blob_data], {
        type: mime_type
    })
    let downloadLink = document.createElement("a");
    downloadLink.download = file_name;
    downloadLink.innerHTML = "Download File";
    downloadLink.href = window.URL.createObjectURL(text);
    downloadLink.click();
}

/**
 * Function assigned to a button to get content of a text area and download it as a Python file.
 * @param {*} elem Button element.
 */
function saveDataContract(elem) {
    let accordion = $(elem).parent().next('div');
    let contract = accordion.find('textarea').val();
    let table_name = accordion.attr('id');

    downloadBlobFile(contract, 'text/x-python', table_name + '_source_data_contract.py')
}

/**
 * Toggles a jQuery element if the value is empty or not.
 * @param {*} element Button element.
 * @param {string} value Value to check if exists.
 */
function toggleDisabledByValue(element, value) {
    if (!value) {
        element.prop('disabled', true)
    } else {
        element.prop('disabled', false)
    }
}

/**
 * Function sets the functionality of a button to login to database given a form value
 * or to get data contracts given a list of tables.
 */
function getTablesButtonAction() {
    $('#db-form').on('submit', function (e) {
        let button = $('#get-tables');
        buttonClickedLoading(button);

        let url = e.target.action;
        let body = getFormDataAsDict($(this).serializeArray());

        authenticatedAjaxRequest(url, 'POST', body).then(function (data) {
            if (data.show_contracts) {
                let accordion = $('#contracts-accordion');
                accordion.empty();
                $.each(data.contracts, function (i, item) {
                    accordion.append([{
                        source: data.source,
                        header: data.tables[i],
                        body: item
                    }].map(Template))
                });
            } else {
                let select = $('#tables-list');
                select.show();
                select.empty();
                $.each(data.tables, function (i, item) {
                    select.append($('<option>', {
                        value: item,
                        text: item
                    }));
                });
                $('#get-all-contracts').prop('disabled', false);
            }

            button.html('Get Data Contracts')
            button.prop('disabled', false);

        }).fail(function (response, text, message) {
            // Modal
            button.html('Get tables list')
            button.prop('disabled', false);
        });


        return false
    });
}

/**
 * Function assgined to a button to get data contract from all tables in database.
 * @param {*} elem Button elemet.
 */
function getAllDataContracts(elem) {
    let button = $(elem);
    buttonClickedLoading(button);

    let body = getFormDataAsDict($('#db-form').serializeArray());
    let url = '/ddl-extractor/all-contracts';

    authenticatedRequest(url, 'POST', body).then(function (data) {
        downloadBlobFile(data, 'application/zip', body["source_name"].toLowerCase() + '_data_contracts.zip');
    }).finally(function () {
        button.html('Get Data Contracts');
        button.prop('disabled', false);
    });


}

$(document).ready(async function () {
    $('#table-name').on('input', function () {
        toggleDisabledByValue($('#get-contracts'), $(this).val());
    });

    getTablesButtonAction();
    document.getElementsByClassName("download-contract").onclick = saveDataContract;
});
