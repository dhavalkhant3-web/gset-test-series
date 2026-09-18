import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';

class FirebaseService {
  static final FirebaseAuth auth = FirebaseAuth.instance;
  static final FirebaseFirestore firestore = FirebaseFirestore.instance;

  static Future<UserCredential> signInWithEmail({
    required String email,
    required String password,
  }) => auth.signInWithEmailAndPassword(email: email.trim(), password: password);

  static Future<UserCredential> registerWithEmail({
    required String email,
    required String password,
  }) => auth.createUserWithEmailAndPassword(email: email.trim(), password: password);

  static Future<void> sendPasswordReset(String email) =>
      auth.sendPasswordResetEmail(email: email.trim());

  static Future<void> signOut() => auth.signOut();

  static Future<void> saveFeedback({
    required String type,
    required String message,
    String? paperId,
    String? questionId,
  }) async {
    final user = auth.currentUser;
    await firestore.collection('feedback').add({
      'uid': user?.uid,
      'email': user?.email,
      'type': type,
      'message': message.trim(),
      'paperId': paperId,
      'questionId': questionId,
      'status': 'new',
      'createdAt': FieldValue.serverTimestamp(),
    });
  }
}
