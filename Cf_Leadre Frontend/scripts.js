document.addEventListener("DOMContentLoaded", () => {
    const leaderboardBody = document.getElementById("leaderboardData");
    const userForm = document.getElementById("userForm");

    // Function to fetch and display leaderboard data
    fetchLeaderboard(); // This will run on page load

    document.getElementById("refreshButton").addEventListener("click", fetchLeaderboard);

    // Function to fetch leaderboard data from API
    async function fetchLeaderboard() {
        try {
            const response = await fetch("http://127.0.0.1:8000/api/leaderboard/");
            const users = await response.json();

            if (!response.ok) {
                throw new Error("Failed to fetch leaderboard");
            }

            leaderboardBody.innerHTML = ""; // Clear existing table

            users.forEach((user, index) => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${index + 1}</td>  
                    <a href="profile.html?id=${user.id}" class="profilelinke profile-link" >${user.name}</a>

                    <td>${user.handle}</td>
                    <td>${user.current_rating}</td>
                    <td>${user.max_rating}</td>
                    <td>${user.batch}</td>
                    <td>${user.roll_number || "Not Get"}</td> 
                    <td>${user.session || "N/A"}</td>
                    <td>${user.address}</td>
                    <td><button class="delete-btn" data-id="${user.id}">❌</button></td>
                `;
                leaderboardBody.appendChild(row);
            });

            // Attach event listeners to delete buttons after rendering
            document.querySelectorAll('.delete-btn').forEach(button => {
                button.addEventListener('click', () => deleteUser(button.getAttribute('data-id')));
            });

        } catch (error) {
            console.error("Error fetching leaderboard:", error);
            alert("Failed to load leaderboard. Check API or server.");
        }
    }

    // Function to add a new user
    async function addUser(event) {
        event.preventDefault(); // Prevent form submission

        const newUser = {
            name: document.getElementById("name").value,
            handle: document.getElementById("handle").value,
            roll_number: document.getElementById("roll_number").value,
            session: document.getElementById("session").value,
            batch: document.getElementById("batch").value,
            address: document.getElementById("address").value,
            profile_pic: document.getElementById("profile_picture").files[0]  // Assuming profilePic is the file input
        };
        console.log(newUser);
        const formData = new FormData();
        formData.append("name", newUser.name);
        formData.append("handle", newUser.handle);
        formData.append("roll_number", newUser.roll_number);
        formData.append("session", newUser.session);
        formData.append("profile_picture", newUser.profile_pic);
        formData.append("batch", newUser.batch);
        formData.append("address", newUser.address);

        try {
            const response = await fetch("http://127.0.0.1:8000/api/leaderboard/", {
                method: "POST",
                body: formData,
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || "Failed to add user");
            }

            alert("User added successfully!");
            userForm.reset();
            fetchLeaderboard(); // Refresh leaderboard
        } catch (error) {
            console.error("Error adding user:", error);
            alert("Failed to add user. Please check input data.");
        }
    }

    // Function to delete a user
    async function deleteUser(userId) {
        if (!confirm("Are you sure you want to delete this user?")) return;

        try {
            const response = await fetch(`http://127.0.0.1:8000/api/leaderboard/${userId}/`, {
                method: "DELETE",
            });

            if (!response.ok) {
                throw new Error("Failed to delete user");
            }

            alert("User deleted successfully!");
            fetchLeaderboard(); // Refresh leaderboard
        } catch (error) {
            console.error("Error deleting user:", error);
            alert("Failed to delete user.");
        }
    }

    // Attach form submit event listener
    userForm.addEventListener("submit", addUser);
});
