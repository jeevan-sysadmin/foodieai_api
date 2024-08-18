from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS
CORS(app)

# Recipe data
recipes = {
    "pasta": [
        "1. Boil water in a pot.",
        "2. Add pasta and cook according to package instructions.",
        "3. In a separate pan, sauté garlic in olive oil.",
        "4. Add vegetables and cook until tender.",
        "5. Drain pasta and mix with the sautéed vegetables.",
        "6. Season with salt, pepper, and herbs."
    ],
    "tamilnadu_biryani": [
        "1. Soak rice for 30 minutes.",
        "2. In a large pot, heat oil and sauté onions, garlic, and ginger.",
        "3. Add chopped tomatoes and cook until soft.",
        "4. Add biryani spices and cook for a minute.",
        "5. Add marinated meat (or vegetables) and cook until done.",
        "6. Add rice and water, and cook until the rice is tender.",
        "7. Garnish with coriander and mint leaves."
    ],
    "mutton_biryani": [
        "1. Soak rice for 30 minutes.",
        "2. Marinate mutton with yogurt, spices, and salt.",
        "3. Heat oil in a pot and cook onions until golden brown.",
        "4. Add garlic, ginger, and marinated mutton. Cook until the mutton is tender.",
        "5. Add chopped tomatoes and cook until soft.",
        "6. Layer the cooked mutton with rice in the pot.",
        "7. Cook on low heat until rice and mutton are fully cooked.",
        "8. Garnish with fried onions, coriander, and mint leaves."
    ]
}

@app.route('/recipe/<dish>', methods=['GET'])
def get_recipe(dish):
    recipe_steps = recipes.get(dish.lower())
    if recipe_steps:
        return jsonify({"dish": dish, "steps": recipe_steps})
    else:
        return jsonify({"error": "Recipe not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

