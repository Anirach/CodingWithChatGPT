const express = require("express");
const cors = require("cors");
const { Sequelize, DataTypes } = require("sequelize");

// Create the Sequelize instance
const sequelize = new Sequelize({
  dialect: "sqlite",
  storage: "library.db",
});

// Define the "books" table
const Book = sequelize.define("Book", {
  title: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  author: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  year: {
    type: DataTypes.INTEGER,
    allowNull: false,
  },
  price: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
});

// Define the "shelves" table
const Shelf = sequelize.define("Shelf", {
  name: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  category: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  libCode: {
    type: DataTypes.STRING,
    allowNull: false,
  },
});

// Define the foreign key relationship between "books" and "shelves"
Book.belongsTo(Shelf);

// Create the Express app
const app = express();

// Enable CORS
app.use(cors());

// Parse JSON request bodies
app.use(express.json());

// Define the routes for the "books" table
app.post("/books", async (req, res) => {
  try {
    const book = await Book.create(req.body);
    res.status(201).json(book);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Failed to create book." });
  }
});

app.get("/books", async (req, res) => {
  try {
    const books = await Book.findAll();
    res.json(books);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Failed to get books." });
  }
});

app.get("/books/:id", async (req, res) => {
  try {
    const book = await Book.findByPk(req.params.id);
    if (book) {
      res.json(book);
    } else {
      res.status(404).json({ error: "Book not found." });
    }
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Failed to get book." });
  }
});

app.put("/books/:id", async (req, res) => {
  try {
    const book = await Book.findByPk(req.params.id);
    if (book) {
      await book.update(req.body);
      res.json(book);
    } else {
      res.status(404).json({ error: "Book not found." });
    }
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Failed to update book." });
  }
});

app.delete("/books/:id", async (req, res) => {
  try {
    const book = await Book.findByPk(req.params.id);
    if (book) {
      await book.destroy();
      res.json({ message: "Book deleted successfully." });
    } else {
      res.status(404).json({ error: "Book not found." });
    }
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Failed to delete book." });
  }
});

// Define the routes for the "shelves" table
app.post("/shelves", async (req, res) => {
  try {
    const shelf = await Shelf.create(req.body);
    res.status(201).json(shelf);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Failed to create shelf." });
  }
});

app.get("/shelves", async (req, res) => {
  try {
    const shelves = await Shelf.findAll();
    res.json(shelves);
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Failed to get shelves." });
  }
});

app.get("/shelves/:id", async (req, res) => {
  try {
    const shelf = await Shelf.findByPk(req.params.id);
    if (shelf) {
      res.json(shelf);
    } else {
      res.status(404).json({ error: "Shelf not found." });
    }
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Failed to get shelf." });
  }
});

app.put("/shelves/:id", async (req, res) => {
  try {
    const shelf = await Shelf.findByPk(req.params.id);
    if (shelf) {
      await shelf.update(req.body);
      res.json(shelf);
    } else {
      res.status(404).json({ error: "Shelf not found." });
    }
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Failed to update shelf." });
  }
});

app.delete("/shelves/:id", async (req, res) => {
  try {
    const shelf = await Shelf.findByPk(req.params.id);
    if (shelf) {
      await shelf.destroy();
      res.json({ message: "Shelf deleted successfully." });
    } else {
      res.status(404).json({ error: "Shelf not found." });
    }
  } catch (err) {
    console.log(err);
    res.status(500).json({ error: "Failed to delete shelf." });
  }
});

// Start the server
sequelize.sync().then(() => {
  app.listen(3000, () => {
    console.log("Server started on port 3000.");
  });
});
