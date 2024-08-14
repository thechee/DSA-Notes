function todoReducer(state, action) {
  switch (action.type) {
    case "ADD_TODO":
      const todos = state.todos;
      return {
        ...state,
        todos: todos.concat(action.payload),
      };
    case "REMOVE_TODO":
      const todos = state.todos;
      const newTodos = todos.filter((todo) => todo.id !== action.id);
      return { ...state, todos: newTodos };
    default:
      return state;
  }
}

function todoReducer(state, action) {
  switch (action.type) {
    case "ADD_TODO": {
      const todos = state.todos;
      return {
        ...state,
        todos: todos.concat(action.payload),
      };
    }
    case "REMOVE_TODO": {
      const todos = state.todos;
      const newTodos = todos.filter((todo) => todo.id !== action.id);
      return { ...state, todos: newTodos };
    }
    default:
      return state;
  }
}
