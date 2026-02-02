import React from 'react';
import { MessageSquare, Heart, Brain, TrendingUp } from 'lucide-react';

/**
 * WelcomeScreen - shown when chat is empty
 */
const WelcomeScreen = () => {
  const features = [
    {
      icon: MessageSquare,
      title: 'Natural Conversation',
      description: 'Chat naturally about your health concerns',
    },
    {
      icon: Brain,
      title: 'AI-Powered Analysis',
      description: 'Advanced ML models analyze your stress levels',
    },
    {
      icon: Heart,
      title: 'Disease Risk Assessment',
      description: 'Get personalized risk analysis for lifestyle diseases',
    },
    {
      icon: TrendingUp,
      title: 'Health Guidance',
      description: 'Receive preventive care recommendations',
    },
  ];

  return (
    <div className="flex-1 flex flex-col items-center justify-center p-8 animate-fade-in">
      <div className="max-w-2xl w-full text-center space-y-8">
        {/* Hero Section */}
        <div className="space-y-4">
          <div className="w-20 h-20 mx-auto rounded-2xl bg-gradient-to-br from-primary-500 to-primary-600 dark:from-primary-400 dark:to-primary-500 flex items-center justify-center shadow-xl">
            <MessageSquare className="w-10 h-10 text-white" strokeWidth={2} />
          </div>
          
          <h2 className="text-3xl md:text-4xl font-display font-bold text-gray-900 dark:text-white">
            Welcome to Stress2Health
          </h2>
          
          <p className="text-lg text-gray-600 dark:text-gray-300 max-w-xl mx-auto leading-relaxed">
            A calm, private space to reflect on stress, understand your risk for lifestyle diseases,
            and receive clear, practical next steps.
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-8">
          {features.map((feature, index) => (
            <div
              key={index}
              className="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl p-5 text-left hover:shadow-lg transition-all duration-200 hover:-translate-y-1"
            >
              <div className="w-10 h-10 rounded-lg bg-primary-100 dark:bg-primary-900/30 flex items-center justify-center mb-3">
                <feature.icon className="w-5 h-5 text-primary-600 dark:text-primary-400" />
              </div>
              <h3 className="font-semibold text-gray-900 dark:text-white mb-1">
                {feature.title}
              </h3>
              <p className="text-sm text-gray-600 dark:text-gray-400">
                {feature.description}
              </p>
            </div>
          ))}
        </div>

        {/* Disclaimer */}
        <div className="bg-amber-50 dark:bg-amber-900/20 border border-amber-200 dark:border-amber-800 rounded-xl p-4 text-sm text-amber-900 dark:text-amber-200">
          <p className="font-medium mb-1">⚠️ Medical Disclaimer</p>
          <p className="text-amber-800 dark:text-amber-300">
            This chatbot provides informational guidance only and is not a substitute 
            for professional medical advice, diagnosis, or treatment.
          </p>
        </div>

        {/* CTA */}
        <p className="text-gray-500 dark:text-gray-400 text-sm">
          Start by typing your message below 👇
        </p>
      </div>
    </div>
  );
};

export default WelcomeScreen;