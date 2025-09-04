import './App.css'

function App() {
  return (
    <div className="App">
      <header>
        <h1>Senha Segura</h1>
      </header>

      <main>
        <section className="login-section">
          <h2>LOGIN</h2>

          <label htmlFor="usuario">Usuário</label>
          <input type="text" name="usuario" id="usuario" />

          <label htmlFor="senha">Senha</label>
          <input type="password" name="senha" id="senha" />

          <button type="submit">Entrar</button>
        </section>
      </main>

      <footer>
        <p>@senha segura</p>
      </footer>
    </div>
  )
}

export default App
