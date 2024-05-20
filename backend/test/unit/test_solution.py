import random
from unittest.mock import patch

from src.static.diets import Diet

import pytest

from src.controllers.recipecontroller import RecipeController


class TestRecipeController:


  # add your test case implementation here
  @pytest.mark.unit
  @patch(
      'src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes')
  @patch('src.util.dao.DAO')
  @patch('src.controllers.recipecontroller.RecipeController.load_recipes')
  def test_normal_take_best_T1(self, mock_rediness, mocked_dao,
      mocked_load_recipes):
    # Test case 1
    mock_rediness.return_value = {"recipe1": 0.5, "recipe2": 0.3}

    mocked_load_recipes.return_value = {"recipe1": 0.5, "recipe2": 0.3}

    recipe_controller = RecipeController(mocked_dao)

    # should be take optimal but is random
    for i in range(100):
        chosen = recipe_controller.get_recipe(Diet.NORMAL, True)
        assert chosen == "recipe1"


  @pytest.mark.unit
  @patch(
      'src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes')
  @patch('src.util.dao.DAO')
  @patch('src.controllers.recipecontroller.RecipeController.load_recipes')
  def test_normal_random_T2(self, mock_rediness, mocked_dao,
      mocked_load_recipes):
      # Test case 2
      random.seed(666)

      recipies = {"recipe1": 0.5, "recipe2": 0.3}

      recipie_names = ["recipe1", "recipe2"]

      mock_rediness.return_value = recipies

      mocked_load_recipes.return_value = recipies

      local_random = random.Random(666)

      for i in range(100):
        recipe_controller = RecipeController(mocked_dao)
        chosen = recipe_controller.get_recipe(Diet.NORMAL, False)
        assert chosen == recipie_names[local_random.randint(0, len(recipie_names)-1)]

  @pytest.mark.unit
  @patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes')
  @patch('src.util.dao.DAO')
  @patch('src.controllers.recipecontroller.RecipeController.load_recipes')
  def test_normal_no_recipies_T3(self, mock_rediness, mocked_dao,
      mocked_load_recipes):
    # Test case 1
    mock_rediness.return_value = {}

    mocked_load_recipes.return_value = {}

    recipe_controller = RecipeController(mocked_dao)
    chosen = recipe_controller.get_recipe(Diet.NORMAL, True)
    assert chosen == None

  @pytest.mark.unit
  @patch('src.controllers.recipecontroller.RecipeController.get_readiness_of_recipes')
  @patch('src.util.dao.DAO')
  @patch('src.controllers.recipecontroller.RecipeController.load_recipes')
  def test_normal_no_recipies_random_T4(self, mock_rediness, mocked_dao,
      mocked_load_recipes):
    # Test case 1
    mock_rediness.return_value = {}

    mocked_load_recipes.return_value = {}

    recipe_controller = RecipeController(mocked_dao)
    chosen = recipe_controller.get_recipe(Diet.NORMAL, False)
    assert chosen == None