export default function localesReducer(state = {}, action) {
  switch (action.type) {
    case "UPDATE_LOCALES":
      return {
        ...state,
        ...action.payload
      };
    default:
      return state;
  }
}
