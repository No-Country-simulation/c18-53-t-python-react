import { createSlice } from '@reduxjs/toolkit';

const userSlice = createSlice({
  name: 'user',
  initialState: {
    name: 'User Test',
    email: 'usertest@gmail.com',
    loggedIn: false,
  },
  reducers: {
    login: (state, action) => {
      state.name = action.payload.name;
      state.email = action.payload.email;
      state.loggedIn = true;
    },
    logout: (state) => {
      state.name = '';
      state.email = '';
      state.loggedIn = false;
    },
    updateUser: (state, action) => {
      const { name, email } = action.payload;
      if (name) state.name = name;
      if (email) state.email = email;
    },
  },
});

export const { login, logout, updateUser } = userSlice.actions;
export default userSlice.reducer;
