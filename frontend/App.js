import React, { useState, useEffect } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Alert, ScrollView } from 'react-native';
import axios from 'axios';

export default function App() {
  const [quiz, setQuiz] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [selected, setSelected] = useState(null);
  const [finished, setFinished] = useState(false);

  useEffect(() => {
    axios.get('http://localhost:5000/api/quiz')  // Use your IP from the Flask log
      .then(res => setQuiz(res.data))
      .catch(() => Alert.alert('Erro', 'Não conseguiu conectar ao servidor. Verifique o backend.'));
  }, []);

  const handleAnswer = (index) => {
    setSelected(index);
    if (quiz[currentIndex]?.alternativas[index]?.correta) {
      setScore(score + 1);
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

  if (quiz.length === 0) return <Text style={styles.center}>Carregando...</Text>;

  if (finished) {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>Quiz terminado!</Text>
        <Text style={styles.score}>Pontuação: {score}/{quiz.length} 🔐</Text>
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

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>🌟 Quiz de Cibersegurança</Text>
      <Text style={styles.progress}>Pergunta {currentIndex + 1} de {quiz.length}</Text>
      <Text style={styles.question}>{q.texto_pergunta}</Text>
      {q.alternativas.map((alt, i) => (
        <TouchableOpacity
          key={i}
          style={[
            styles.option,
            selected === i && (alt.correta ? styles.correct : styles.wrong)
          ]}
          onPress={() => handleAnswer(i)}
          disabled={selected !== null}
        >
          <Text style={styles.optionText}>{letters[i]}) {alt.texto_alternativa}</Text>
        </TouchableOpacity>
      ))}
      {selected !== null && (
        <TouchableOpacity style={styles.button} onPress={nextQuestion}>
          <Text style={styles.buttonText}>Próxima →</Text>
        </TouchableOpacity>
      )}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flexGrow: 1, padding: 20, backgroundColor: '#f0f0f0' },
  center: { flex: 1, textAlign: 'center', marginTop: 50, fontSize: 18 },
  title: { fontSize: 24, fontWeight: 'bold', textAlign: 'center', marginBottom: 20 },
  progress: { fontSize: 18, textAlign: 'center', marginBottom: 20 },
  question: { fontSize: 18, marginBottom: 30, textAlign: 'center' },
  option: { backgroundColor: 'white', padding: 15, borderRadius: 10, marginBottom: 10 },
  optionText: { fontSize: 16 },
  correct: { backgroundColor: '#d4edda', borderColor: '#c3e6cb' },
  wrong: { backgroundColor: '#f8d7da', borderColor: '#f5c6cb' },
  button: { backgroundColor: '#007bff', padding: 15, borderRadius: 10, alignItems: 'center', marginTop: 20 },
  buttonText: { color: 'white', fontSize: 18, fontWeight: 'bold' },
  score: { fontSize: 28, textAlign: 'center', marginVertical: 30 },
});