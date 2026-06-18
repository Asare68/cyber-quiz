/*
import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Alert, TextInput, ScrollView } from 'react-native';
import axios from 'axios';

export default function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [token, setToken] = useState(null);

  const [quiz, setQuiz] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [selected, setSelected] = useState(null);
  const [finished, setFinished] = useState(false);
  const [loading, setLoading] = useState(false);

  /*const handleLogin = async () => {
    if (!email || !password) {
      Alert.alert('Erro', 'Preencha email e senha');
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/api/login', {
        email: email,
        password: password
      });

      if (response.status === 200) {
        setToken(response.data.token);
        setIsLoggedIn(true);
        Alert.alert('Sucesso', 'Login realizado!');
        loadQuiz();
      }
    } catch (error) {
      Alert.alert('Erro', 'Falha no login');
    } finally {
      setLoading(false);
    }
  }; */

 /* // Fix 1: Await loadQuiz properly and guard against bad data
const handleLogin = async () => {
  if (!email || !password) {
    Alert.alert('Erro', 'Preencha email e senha');
    return;
  }
  setLoading(true);
  try {
    const response = await axios.post('http://localhost:5000/api/login', {
      email, password
    });
    if (response.status === 200) {
      setToken(response.data.token);
      await loadQuiz(); // ✅ await it before setting logged in
      setIsLoggedIn(true);
    }
  } catch (error) {
    Alert.alert('Erro', 'Falha no login');
  } finally {
    setLoading(false);
  }
};



  const loadQuiz = async () => {
    try {
      const res = await axios.get('http://localhost:5000/api/quiz');
      setQuiz(res.data);
    } catch (e) {
      Alert.alert('Erro', 'Não conseguiu carregar o quiz');
    }
  };

  const handleAnswer = (index) => {
    setSelected(index);
    if (quiz[currentIndex]?.respostas[index]?.e_correta) {
      setScore(score + 1);
      Alert.alert('🎉', 'Correto!');
    } else {
      Alert.alert('😕', 'Errado!');
    }
  };

/*const nextQuestion = () => {

    console.log("currentIndex:", currentIndex, "quiz length:", quiz.length);
    const isLast = currentIndex + 1 >= quiz.length;

    if (isLast) {
      setFinished(true);
    } else {
      setSelected(null);
      setCurrentIndex(currentIndex + 1);
    }
  };*/

/*
  const nextQuestion = () => {
    console.log("currentIndex:", currentIndex, "quiz length:", quiz.length);
    setSelected(null);
    if (currentIndex + 1 < quiz.length) {
      setCurrentIndex(currentIndex + 1);
    } else {
      setFinished(true);
    }
  };
  

  // Login Screen
  if (!isLoggedIn) {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>🌟 Quiz de Cibersegurança</Text>
        <Text style={styles.subtitle}>Faça login para começar</Text>
        
        <TextInput style={styles.input} placeholder="Email" value={email} onChangeText={setEmail} keyboardType="email-address" autoCapitalize="none" />
        <TextInput style={styles.input} placeholder="Senha" value={password} onChangeText={setPassword} secureTextEntry />
        
        <TouchableOpacity style={styles.button} onPress={handleLogin} disabled={loading}>
          <Text style={styles.buttonText}>{loading ? "Entrando..." : "Entrar"}</Text>
        </TouchableOpacity>
      </View>
    );
  }

  if (quiz.length === 0) return <Text style={styles.center}>Carregando...</Text>;

 /* if (finished) {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>Quiz terminado!</Text>
        <Text style={styles.score}>Pontuação: {score}/{quiz.length}</Text>
        <TouchableOpacity style={styles.button} onPress={() => {
          setCurrentIndex(0); setScore(0); setFinished(false); setSelected(null);
        }}>
          <Text style={styles.buttonText}>Jogar Novamente</Text>
        </TouchableOpacity>
      </View>
    );
  }*/

 /*   // Fix 2: Add emoji feedback to the finished screen
if (finished) {
  const percentage = score / quiz.length;
  const emoji =
    percentage === 1 ? '🏆' :
    percentage >= 0.7 ? '🎉' :
    percentage >= 0.4 ? '😊' : '😕';

  const message =
    percentage === 1 ? 'Perfeito!' :
    percentage >= 0.7 ? 'Muito bem!' :
    percentage >= 0.4 ? 'Bom esforço!' : 'Continue praticando!';

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Quiz Terminado!</Text>
      <Text style={{ fontSize: 80, textAlign: 'center', marginVertical: 20 }}>
        {emoji}
      </Text>
      <Text style={styles.score}>
        {score}/{quiz.length}
      </Text>
      <Text style={{ fontSize: 22, textAlign: 'center', marginBottom: 30 }}>
        {message}
      </Text>
      <TouchableOpacity style={styles.button} onPress={() => {
        setCurrentIndex(0); setScore(0); setFinished(false); setSelected(null);
      }}>
        <Text style={styles.buttonText}>Jogar Novamente</Text>
      </TouchableOpacity>
    </View>
  );
}





  const q = quiz[currentIndex];
  const letters = ['A', 'B', 'C', 'D'];

 /* return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>🌟 Quiz de Cibersegurança</Text>
      <Text style={styles.progress}>Pergunta {currentIndex + 1} de {quiz.length}</Text>
      <Text style={styles.question}>{q.conteudo}</Text>
     
  {q.respostas.map((resp, i) => (
        <TouchableOpacity
          key={i}
          style={[styles.option, selected === i && (resp.e_correta ? styles.correct : styles.wrong)]}
          onPress={() => handleAnswer(i)}
          disabled={selected !== null}
        >
          <Text style={styles.optionText}>{letters[i]}) {resp.texto}</Text>
        </TouchableOpacity>
      ))}
      
      {selected !== null && (
        <TouchableOpacity style={styles.button} onPress={nextQuestion}>
          <Text style={styles.buttonText}>Próxima →</Text>
        </TouchableOpacity>
      )}
    </ScrollView>
  );*/
/*
   return (
     <div>
      <h2>Resultados do Quiz</h2>
     {scores && Array.isArray(scores) && scores.length > 0 ? (
        scores.map((score, index) => (
          <div key={index}>
             Pontuação: {score}{" "}
            {score >= 80 ? "🎉 Mandou bem!" : "😅 Continue praticando!"}
          </div>
        ))
      ) : (
        <p>Nenhuma pontuação disponível</p>
     )}
   </div>
  );
 }
 
 ;
 
// Opcional: se quiser mostrar perguntas e respostas também
// {results && results.map((item, index) => (
//   <div key={index}>
//     Pergunta {index + 1}: {item.question} <br />//     Sua resposta: {item.answer} {item.score >= 80 ? "🎉" : "😅"}





const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, backgroundColor: '#f0f0f0' },
  title: { fontSize: 24, fontWeight: 'bold', textAlign: 'center', marginBottom: 20 },
  subtitle: { fontSize: 18, textAlign: 'center', marginBottom: 20 },
  input: { backgroundColor: 'white', padding: 15, borderRadius: 10, marginBottom: 15, fontSize: 16 },
  question: { fontSize: 18, marginBottom: 30, textAlign: 'center' },
  progress: { fontSize: 18, textAlign: 'center', marginBottom: 20 },
  option: { backgroundColor: 'white', padding: 15, borderRadius: 10, marginBottom: 10 },
  optionText: { fontSize: 16 },
  correct: { backgroundColor: '#d4edda' },
  wrong: { backgroundColor: '#f8d7da' },
  button: { backgroundColor: '#007bff', padding: 15, borderRadius: 10, alignItems: 'center', marginTop: 20 },
  buttonText: { color: 'white', fontSize: 18, fontWeight: 'bold' },
  score: { fontSize: 28, textAlign: 'center', marginVertical: 30 },
  center: { flex: 1, textAlign: 'center', marginTop: 100, fontSize: 18 }
}) ;



*/

import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Alert, TextInput, ScrollView } from 'react-native';
import axios from 'axios';

export default function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [token, setToken] = useState(null);

  const [quiz, setQuiz] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [selected, setSelected] = useState(null);
  const [finished, setFinished] = useState(false);
  const [loading, setLoading] = useState(false);

  const loadQuiz = async () => {
    try {
      const res = await axios.get('http://localhost:5000/api/quiz');
      // ✅ THE FIX: filter out the tema object at the end of the array
      // Your API returns 12 items but the last one is {"id_tema":1,"nome_tema":"..."}
      // which has no "conteudo" or "respostas" — that was causing the crash
      const questionsOnly = res.data.filter(
        item => item.conteudo && Array.isArray(item.respostas)
      );
      setQuiz(questionsOnly);
    } catch (e) {
      Alert.alert('Erro', 'Não conseguiu carregar o quiz');
    }
  };

  const handleLogin = async () => {
    if (!email || !password) {
      Alert.alert('Erro', 'Preencha email e senha');
      return;
    }
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/api/login', { email, password });
      if (response.status === 200) {
        setToken(response.data.token);
        await loadQuiz();
        setIsLoggedIn(true);
      } else if (response.status === 401) {
        console.log('Credenciais inválidas');
      }
    } catch (error) {
      Alert.alert('Erro', 'Falha no login');
    } finally {
      setLoading(false);
    }
  };

  const handleAnswer = (index) => {
    if (selected !== null) return;
    setSelected(index);
    if (quiz[currentIndex]?.respostas[index]?.e_correta) {
      setScore((prev) => prev + 1);
      Alert.alert('🎉', 'Correto!');
    } else {
      Alert.alert('😕', 'Errado!');
    }
  };

  const nextQuestion = () => {
    setSelected(null);
    if (currentIndex + 1 < quiz.length) {
      setCurrentIndex(currentIndex + 1);
    } else {
      setFinished(true);
    }
  };

  const restartQuiz = () => {
    setCurrentIndex(0);
    setScore(0);
    setFinished(false);
    setSelected(null);
  };

  // ─── LOGIN SCREEN ───────────────────────────────────────────────
  if (!isLoggedIn) {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>🌟 Quiz de Cibersegurança</Text>
        <Text style={styles.subtitle}>Faça login para começar</Text>
        <TextInput
          style={styles.input}
          placeholder="Email"
          value={email}
          onChangeText={setEmail}
          keyboardType="email-address"
          autoCapitalize="none"
        />
        <TextInput
          style={styles.input}
          placeholder="Senha"
          value={password}
          onChangeText={setPassword}
          secureTextEntry
        />
        <TouchableOpacity style={styles.button} onPress={handleLogin} disabled={loading}>
          <Text style={styles.buttonText}>{loading ? 'Entrando...' : 'Entrar'}</Text>
        </TouchableOpacity>
      </View>
    );
  }

  // ─── LOADING SCREEN ─────────────────────────────────────────────
  if (quiz.length === 0) {
    return (
      <View style={styles.container}>
        <Text style={styles.center}>Carregando quiz... ⏳</Text>
      </View>
    );
  }

  // ─── SCORE SCREEN ───────────────────────────────────────────────
  if (finished) {
    const percentage = score / quiz.length;

    const emoji =
      percentage === 1 ? '🏆' :
      percentage >= 0.7 ? '🎉' :
      percentage >= 0.4 ? '😊' : '😕';

    const message =
      percentage === 1 ? 'Perfeito! Você acertou tudo!' :
      percentage >= 0.7 ? 'Muito bem! Ótimo resultado!' :
      percentage >= 0.4 ? 'Bom esforço! Continue praticando!' :
      'Não desista! Tente novamente!';

    const scoreColor =
      percentage === 1 ? '#28a745' :
      percentage >= 0.7 ? '#17a2b8' :
      percentage >= 0.4 ? '#e6a817' : '#dc3545';

    return (
      <View style={styles.container}>
        <Text style={styles.title}>Quiz Terminado! 🎯</Text>

        <Text style={styles.bigEmoji}>{emoji}</Text>

        <Text style={[styles.scoreNumber, { color: scoreColor }]}>
          {score}/{quiz.length}
        </Text>

        <View style={styles.barBackground}>
          <View style={[styles.barFill, {
            width: `${Math.round(percentage * 100)}%`,
            backgroundColor: scoreColor,
          }]} />
        </View>

        <Text style={styles.percentText}>{Math.round(percentage * 100)}% correto</Text>

        <Text style={styles.message}>{message}</Text>

        <TouchableOpacity style={styles.button} onPress={restartQuiz}>
          <Text style={styles.buttonText}>🔄 Jogar Novamente</Text>
        </TouchableOpacity>
      </View>
    );
  }

  // ─── QUIZ SCREEN ────────────────────────────────────────────────
  const q = quiz[currentIndex];
  const letters = ['A', 'B', 'C', 'D'];

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>🌟 Quiz de Cibersegurança</Text>
      <Text style={styles.progress}>Pergunta {currentIndex + 1} de {quiz.length}</Text>

      <View style={styles.barBackground}>
        <View style={[styles.barFill, {
          width: `${Math.round((currentIndex / quiz.length) * 100)}%`,
          backgroundColor: '#007bff',
        }]} />
      </View>

      <Text style={styles.question}>{q.conteudo}</Text>

      {q.respostas.map((resp, i) => (
        <TouchableOpacity
          key={i}
          style={[
            styles.option,
            selected !== null && resp.e_correta && styles.correct,
            selected === i && !resp.e_correta && styles.wrong,
          ]}
          onPress={() => handleAnswer(i)}
          disabled={selected !== null}
        >
          <Text style={styles.optionText}>{letters[i]}) {resp.texto}</Text>
        </TouchableOpacity>
      ))}

      {selected !== null && (
        <TouchableOpacity style={styles.button} onPress={nextQuestion}>
          <Text style={styles.buttonText}>
            {currentIndex + 1 < quiz.length ? 'Próxima →' : 'Ver Resultado 🏁'}
          </Text>
        </TouchableOpacity>
      )}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    padding: 24,
    backgroundColor: '#f0f4f8',
    justifyContent: 'center',
  },
  title: {
    fontSize: 22,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 10,
    color: '#1a1a2e',
  },
  subtitle: {
    fontSize: 16,
    textAlign: 'center',
    marginBottom: 30,
    color: '#555',
  },
  input: {
    backgroundColor: 'white',
    padding: 15,
    borderRadius: 10,
    marginBottom: 15,
    fontSize: 16,
    borderWidth: 1,
    borderColor: '#ddd',
  },
  question: {
    fontSize: 18,
    marginVertical: 20,
    textAlign: 'center',
    fontWeight: '600',
    color: '#1a1a2e',
    lineHeight: 26,
  },
  progress: {
    fontSize: 14,
    textAlign: 'center',
    marginBottom: 6,
    color: '#666',
  },
  option: {
    backgroundColor: 'white',
    padding: 15,
    borderRadius: 10,
    marginBottom: 10,
    borderWidth: 1,
    borderColor: '#ddd',
  },
  optionText: {
    fontSize: 16,
    color: '#333',
  },
  correct: {
    backgroundColor: '#d4edda',
    borderColor: '#28a745',
  },
  wrong: {
    backgroundColor: '#f8d7da',
    borderColor: '#dc3545',
  },
  button: {
    backgroundColor: '#007bff',
    padding: 15,
    borderRadius: 10,
    alignItems: 'center',
    marginTop: 20,
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: 'bold',
  },
  bigEmoji: {
    fontSize: 100,
    textAlign: 'center',
    marginVertical: 20,
  },
  scoreNumber: {
    fontSize: 56,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 10,
  },
  percentText: {
    fontSize: 16,
    textAlign: 'center',
    color: '#555',
    marginTop: 6,
    marginBottom: 4,
  },
  message: {
    fontSize: 20,
    textAlign: 'center',
    marginVertical: 20,
    color: '#333',
    fontWeight: '500',
  },
  barBackground: {
    height: 10,
    backgroundColor: '#ddd',
    borderRadius: 5,
    overflow: 'hidden',
    marginVertical: 6,
  },
  barFill: {
    height: '100%',
    borderRadius: 5,
  },
  center: {
    textAlign: 'center',
    fontSize: 18,
    color: '#555',
    marginTop: 100,
  },
});