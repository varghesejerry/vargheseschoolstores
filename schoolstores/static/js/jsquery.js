function updateCourseOptions() {
                var departmentSelect = document.getElementById("department");
                var specializationSelect = document.getElementById("specialization");
                var selectedDepartment = departmentSelect.value;

                // Reset the specialization dropdown
                specializationSelect.innerHTML = '<option value="" disabled selected>Select your specialization</option>';
                specializationSelect.disabled = true;

                if (selectedDepartment === "computer-science") {
                    addOption(specializationSelect, "data-science", "Data Science");
                    addOption(specializationSelect, "software-engineering", "Software Engineering");
                } else if (selectedDepartment === "electronics") {
                    addOption(specializationSelect, "embedded-systems", "Embedded Systems");
                    addOption(specializationSelect, "communication-engineering", "Communication Engineering");
                } else if (selectedDepartment === "mechanical") {
                    addOption(specializationSelect, "automobile-engineering", "Automobile Engineering");
                    addOption(specializationSelect, "thermal-engineering", "Thermal Engineering");
                } else if (selectedDepartment === "commerce") {
                    addOption(specializationSelect, "bcom", "Bcom");
                    addOption(specializationSelect, "bba", "BBA");
                } else if (selectedDepartment === "biomaths") {
                    addOption(specializationSelect, "biotechnology", "Biotechnology");
                    addOption(specializationSelect, "microbiology", "Microbiology");
                }

                specializationSelect.disabled = false;
            }

            function addOption(selectElement, value, text) {
                var option = document.createElement("option");
                option.value = value;
                option.text = text;
                selectElement.add(option);
            }