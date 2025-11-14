import { combineReducers } from "redux";
import { intlReducer } from "react-intl-redux";
import localesReducer from "./locales";

const reducers = combineReducers({
  locales: localesReducer,
  intl: intlReducer
});

export default reducers;
