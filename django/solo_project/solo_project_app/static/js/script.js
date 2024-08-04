
function toggleCustomRoleInput() {
    var roleSelect = document.getElementById('role');
    var customRoleContainer = document.getElementById('custom-role-container');
    var customDescriptionContainer = document.getElementById('custom-description-container');
    if (roleSelect.value === 'custom') {
        customRoleContainer.style.display = 'block';
        customDescriptionContainer.style.display = 'block';
    } else {
        customRoleContainer.style.display = 'none';
        customDescriptionContainer.style.display = 'none';
    }
}