import { createStore } from "redux";
import { persistReducer, persistStore } from "redux-persist";
import storage from "redux-persist/lib/storage";
import reducers from "../modules";
import flatten from "flat";
import ja from "../i18n/language/ja";
import en from "../i18n/language/en";
import { updateIntl } from "react-intl-redux";


const messages = {
  ja,
  en
};

const initialState = {
  intl: {
    locale: "ja",
    messages: flatten(ja)
  }
};

const persistConfig = {
  key: `final-sequence`,
  blacklist: "intl.messages",
  storage
};

const persistedReducer = persistReducer(persistConfig, reducers);

const store = createStore(
  persistedReducer,
  initialState,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);
const persistor = persistStore(store);

const changeLanguage = languageCode => {
  store.dispatch(
    updateIntl({
      locale: languageCode,
      messages: flatten(messages[languageCode])
    })
  );
};
export default store;
export { persistor, changeLanguage };
