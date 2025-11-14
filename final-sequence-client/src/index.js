import React from "react";
import { render } from "react-dom";
import { Provider } from "react-redux";
import { PersistGate } from "redux-persist/integration/react";

import store, { persistor } from "./stores";
import App from "./pages/App";
import { IntlProvider } from "react-intl-redux";

render(
  <Provider store={store}>
    <IntlProvider>
      <PersistGate loading={null} persistor={persistor}>
        <App />
      </PersistGate>
    </IntlProvider>
  </Provider>,
  document.getElementById("root")
);
