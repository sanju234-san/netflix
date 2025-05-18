const express = require("express");
const cors = require("cors");
const fs = require("fs");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 5000; // Allow custom port if needed

// ✅ Middleware
app.use(cors({
  origin: "http://localhost:3000", // Ensure only frontend allowed
  credentials: true,
}));
app.use(express.json());

// ✅ Directory to store face descriptors
const FACE_DATA_DIR = path.join(__dirname, "faces");
if (!fs.existsSync(FACE_DATA_DIR)) {
  fs.mkdirSync(FACE_DATA_DIR);
}

// ✅ In-memory user database
const users = [
  { username: "admin", password: "1234" },
  { username: "user1", password: "abcd" },
];

// ✅ Root route
app.get("/", (req, res) => {
  res.send("✅ Face Auth backend is running.");
});

// ✅ Manual Login
app.post("/auth/login", (req, res) => {
  const { username, password } = req.body;
  if (!username || !password) {
    return res.status(400).json({ message: "Username and password are required." });
  }

  const user = users.find(u => u.username === username && u.password === password);
  if (user) {
    return res.status(200).json({ message: "Login successful", token: "abc123", user: username });
  }

  res.status(401).json({ message: "Invalid username or password." });
});

// ✅ Register Face Descriptor
app.post("/auth/register-face", (req, res) => {
  const { username, descriptor } = req.body;
  if (!username || !descriptor || !Array.isArray(descriptor)) {
    return res.status(400).json({ message: "Username and valid face descriptor are required." });
  }

  try {
    const filePath = path.join(FACE_DATA_DIR, `${username}.json`);
    fs.writeFileSync(filePath, JSON.stringify(descriptor));
    res.status(200).json({ message: "Face registered successfully." });
  } catch (err) {
    res.status(500).json({ message: "Error saving face descriptor.", error: err.message });
  }
});

// ✅ Face Login with Cosine Similarity
app.post("/auth/face-login", (req, res) => {
  const { descriptor } = req.body;
  if (!descriptor || !Array.isArray(descriptor)) {
    return res.status(400).json({ message: "Valid face descriptor is required." });
  }

  try {
    const files = fs.readdirSync(FACE_DATA_DIR);
    let matchedUser = null;

    for (const file of files) {
      const storedDescriptor = JSON.parse(fs.readFileSync(path.join(FACE_DATA_DIR, file)));
      const similarity = cosineSimilarity(descriptor, storedDescriptor);

      if (similarity >= 0.95) {
        matchedUser = path.basename(file, ".json");
        break;
      }
    }

    if (matchedUser) {
      res.status(200).json({ message: "Face login successful", user: matchedUser });
    } else {
      res.status(401).json({ message: "Face not recognized." });
    }
  } catch (err) {
    res.status(500).json({ message: "Error during face login.", error: err.message });
  }
});

// ✅ Cosine Similarity Function
function cosineSimilarity(a, b) {
  const dot = a.reduce((sum, v, i) => sum + v * b[i], 0);
  const magA = Math.sqrt(a.reduce((sum, v) => sum + v * v, 0));
  const magB = Math.sqrt(b.reduce((sum, v) => sum + v * v, 0));
  return dot / (magA * magB);
}

// ✅ Start Server
app.listen(PORT, () => {
  console.log(`✅ Server running at http://localhost:${PORT}`);
});
