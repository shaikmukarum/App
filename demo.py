<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rural Health - Healthcare in Your Pocket</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
            text-align: center;
        }

        .header h1 {
            color: #4a5568;
            font-size: 2.5rem;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .header p {
            color: #718096;
            font-size: 1.1rem;
        }

        .nav-tabs {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            margin-bottom: 30px;
        }

        .nav-tab {
            background: rgba(255, 255, 255, 0.9);
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .nav-tab.active {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        }

        .nav-tab:hover:not(.active) {
            background: rgba(255, 255, 255, 1);
            transform: translateY(-1px);
        }

        .content-section {
            display: none;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        }

        .content-section.active {
            display: block;
            animation: fadeIn 0.5s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .form-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #4a5568;
        }

        .form-group input, 
        .form-group select, 
        .form-group textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #e2e8f0;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s ease;
        }

        .form-group input:focus, 
        .form-group select:focus, 
        .form-group textarea:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        .btn {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 25px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-right: 10px;
            margin-bottom: 10px;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        }

        .btn-secondary {
            background: linear-gradient(135deg, #48bb78, #38a169);
        }

        .btn-danger {
            background: linear-gradient(135deg, #f56565, #e53e3e);
        }

        .card {
            background: rgba(247, 250, 252, 0.8);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            border-left: 4px solid #667eea;
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateX(5px);
        }

        .card h3 {
            color: #4a5568;
            margin-bottom: 10px;
        }

        .symptoms-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            margin: 20px 0;
        }

        .symptom-checkbox {
            display: flex;
            align-items: center;
            background: rgba(247, 250, 252, 0.8);
            padding: 10px;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        .symptom-checkbox:hover {
            background: rgba(102, 126, 234, 0.1);
        }

        .symptom-checkbox input {
            margin-right: 10px;
        }

        .ai-result, .prescription, .records-display {
            background: linear-gradient(135deg, rgba(72, 187, 120, 0.1), rgba(56, 161, 105, 0.1));
            border: 2px solid #48bb78;
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
        }

        .pharmacy-card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #48bb78;
        }

        .pharmacy-card h4 {
            color: #4a5568;
            margin-bottom: 10px;
        }

        .medicine-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            background: rgba(247, 250, 252, 0.8);
            border-radius: 8px;
            margin-bottom: 10px;
        }

        .status {
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 600;
        }

        .status.available {
            background: rgba(72, 187, 120, 0.2);
            color: #38a169;
        }

        .status.low-stock {
            background: rgba(237, 137, 54, 0.2);
            color: #c05621;
        }

        .status.out-of-stock {
            background: rgba(245, 101, 101, 0.2);
            color: #e53e3e;
        }

        .qr-scanner {
            text-align: center;
            padding: 40px;
            border: 2px dashed #667eea;
            border-radius: 12px;
            background: rgba(102, 126, 234, 0.05);
            margin: 20px 0;
        }

        .language-selector {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 8px;
            padding: 8px;
        }

        .video-call {
            background: #1a202c;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            color: white;
            margin: 20px 0;
        }

        .doctor-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .doctor-card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .doctor-card:hover {
            transform: translateY(-5px);
        }

        .doctor-avatar {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea, #764ba2);
            margin: 0 auto 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 30px;
            font-weight: bold;
        }

        .emergency-banner {
            background: linear-gradient(135deg, #f56565, #e53e3e);
            color: white;
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 20px;
            font-weight: 600;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.8; }
            100% { opacity: 1; }
        }

        .delivery-tracking {
            background: white;
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .tracking-step {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            padding: 10px;
            border-radius: 8px;
        }

        .tracking-step.completed {
            background: rgba(72, 187, 120, 0.1);
        }

        .tracking-step.active {
            background: rgba(102, 126, 234, 0.1);
        }

        .step-icon {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            margin-right: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
        }

        .step-icon.completed {
            background: #48bb78;
            color: white;
        }

        .step-icon.active {
            background: #667eea;
            color: white;
        }

        .step-icon.pending {
            background: #e2e8f0;
            color: #718096;
        }

        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }
            
            .header h1 {
                font-size: 1.8rem;
            }
            
            .form-grid {
                grid-template-columns: 1fr;
            }
            
            .nav-tabs {
                flex-direction: column;
                align-items: center;
            }
            
            .nav-tab {
                width: 200px;
            }
        }
    </style>
</head>
<body>
    <div class="language-selector">
        <select id="languageSelect">
            <option value="en">English</option>
            <option value="hi">हिंदी</option>
            <option value="te">తెలుగు</option>
            <option value="ta">தமிழ்</option>
            <option value="bn">বাংলা</option>
        </select>
    </div>

    <div class="container">
        <div class="header">
            <h1>🏥 Rural Health Platform</h1>
            <p>Healthcare in Your Pocket - Doctor, AI, Pharmacy & Records Accessible Anytime, Anywhere</p>
        </div>

        <div class="nav-tabs">
            <button class="nav-tab active" onclick="showSection('ai-checker')">🤖 AI Health Checker</button>
            <button class="nav-tab" onclick="showSection('telemedicine')">👨‍⚕️ Doctor Consultation</button>
            <button class="nav-tab" onclick="showSection('pharmacy')">💊 Pharmacy & Delivery</button>
            <button class="nav-tab" onclick="showSection('records')">📋 Health Records</button>
            <button class="nav-tab" onclick="showSection('emergency')">🚨 Emergency</button>
        </div>

        <!-- AI Health Checker Section -->
        <div id="ai-checker" class="content-section active">
            <h2>🤖 AI Health Checker</h2>
            <p>Describe your symptoms and get instant AI-powered health guidance</p>

            <div class="form-grid">
                <div>
                    <div class="form-group">
                        <label>Patient Information</label>
                        <input type="text" id="patientName" placeholder="Full Name">
                    </div>
                    <div class="form-group">
                        <label>Age</label>
                        <input type="number" id="patientAge" placeholder="Age">
                    </div>
                    <div class="form-group">
                        <label>Gender</label>
                        <select id="patientGender">
                            <option value="">Select Gender</option>
                            <option value="male">Male</option>
                            <option value="female">Female</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                </div>
                <div>
                    <div class="form-group">
                        <label>Primary Symptoms (Describe in your language)</label>
                        <textarea id="symptoms" rows="4" placeholder="Describe your symptoms in detail..."></textarea>
                    </div>
                </div>
            </div>

            <h3>Common Symptoms (Check all that apply)</h3>
            <div class="symptoms-grid">
                <label class="symptom-checkbox">
                    <input type="checkbox" value="fever"> Fever
                </label>
                <label class="symptom-checkbox">
                    <input type="checkbox" value="headache"> Headache
                </label>
                <label class="symptom-checkbox">
                    <input type="checkbox" value="cough"> Cough
                </label>
                <label class="symptom-checkbox">
                    <input type="checkbox" value="fatigue"> Fatigue
                </label>
                <label class="symptom-checkbox">
                    <input type="checkbox" value="nausea"> Nausea
                </label>
                <label class="symptom-checkbox">
                    <input type="checkbox" value="bodyache"> Body Ache
                </label>
                <label class="symptom-checkbox">
                    <input type="checkbox" value="breathlessness"> Breathlessness
                </label>
                <label class="symptom-checkbox">
                    <input type="checkbox" value="chestpain"> Chest Pain
                </label>
            </div>

            <button class="btn" onclick="analyzeSymptoms()">🔍 Analyze Symptoms</button>
            <button class="btn btn-secondary" onclick="voiceInput()">🎤 Voice Input</button>

            <div id="aiResult" class="ai-result" style="display: none;">
                <h3>🤖 AI Analysis Result</h3>
                <div id="analysisContent"></div>
            </div>
        </div>

        <!-- Telemedicine Section -->
        <div id="telemedicine" class="content-section">
            <h2>👨‍⚕️ Doctor Consultation</h2>
            <p>Connect with qualified doctors via video call or schedule appointments</p>

            <div class="form-grid">
                <div>
                    <div class="form-group">
                        <label>Consultation Type</label>
                        <select id="consultationType">
                            <option value="general">General Medicine</option>
                            <option value="pediatric">Pediatrics</option>
                            <option value="gynecology">Gynecology</option>
                            <option value="cardiology">Cardiology</option>
                            <option value="dermatology">Dermatology</option>
                            <option value="mental">Mental Health</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Preferred Language</label>
                        <select id="consultationLanguage">
                            <option value="english">English</option>
                            <option value="hindi">Hindi</option>
                            <option value="telugu">Telugu</option>
                            <option value="tamil">Tamil</option>
                            <option value="bengali">Bengali</option>
                        </select>
                    </div>
                </div>
                <div>
                    <div class="form-group">
                        <label>Brief Description of Problem</label>
                        <textarea id="consultationProblem" rows="4" placeholder="Describe your health concern..."></textarea>
                    </div>
                </div>
            </div>

            <button class="btn" onclick="startVideoCall()">📹 Start Video Consultation</button>
            <button class="btn btn-secondary" onclick="scheduleAppointment()">📅 Schedule Appointment</button>

            <div class="doctor-list">
                <div class="doctor-card">
                    <div class="doctor-avatar">Dr</div>
                    <h4>Dr. Priya Sharma</h4>
                    <p>General Medicine</p>
                    <p>⭐ 4.8 (124 reviews)</p>
                    <p>💬 Hindi, English</p>
                    <button class="btn">Consult Now</button>
                </div>
                <div class="doctor-card">
                    <div class="doctor-avatar">Dr</div>
                    <h4>Dr. Rajesh Kumar</h4>
                    <p>Pediatrics</p>
                    <p>⭐ 4.9 (89 reviews)</p>
                    <p>💬 Telugu, Hindi</p>
                    <button class="btn">Consult Now</button>
                </div>
                <div class="doctor-card">
                    <div class="doctor-avatar">Dr</div>
                    <h4>Dr. Anjali Patel</h4>
                    <p>Gynecology</p>
                    <p>⭐ 4.7 (156 reviews)</p>
                    <p>💬 English, Tamil</p>
                    <button class="btn">Consult Now</button>
                </div>
            </div>

            <div id="videoCall" class="video-call" style="display: none;">
                <h3>📹 Video Consultation Active</h3>
                <p>Connected with Dr. Priya Sharma</p>
                <button class="btn btn-danger" onclick="endCall()">End Call</button>
            </div>
        </div>

        <!-- Pharmacy Section -->
        <div id="pharmacy" class="content-section">
            <h2>💊 Pharmacy & Medicine Delivery</h2>
            <p>Check medicine availability and get doorstep delivery</p>

            <div class="form-group">
                <label>Search Medicine</label>
                <input type="text" id="medicineSearch" placeholder="Enter medicine name..." oninput="searchMedicine()">
            </div>

            <div id="pharmacyResults">
                <div class="pharmacy-card">
                    <h4>🏪 Sharma Medical Store</h4>
                    <p>📍 Village Center, 0.8 km away</p>
                    <p>📞 +91 98765 43210</p>
                    
                    <div class="medicine-item">
                        <div>
                            <strong>Paracetamol 500mg</strong>
                            <br><small>Strip of 10 tablets</small>
                        </div>
                        <div>
                            <span class="status available">Available</span>
                            <strong>₹12</strong>
                        </div>
                    </div>
                    
                    <div class="medicine-item">
                        <div>
                            <strong>Crocin Advance</strong>
                            <br><small>Strip of 15 tablets</small>
                        </div>
                        <div>
                            <span class="status low-stock">Low Stock</span>
                            <strong>₹28</strong>
                        </div>
                    </div>
                    
                    <button class="btn">🛒 Order from this store</button>
                </div>

                <div class="pharmacy-card">
                    <h4>🏪 Krishna Pharmacy</h4>
                    <p>📍 Main Road, 1.2 km away</p>
                    <p>📞 +91 87654 32109</p>
                    
                    <div class="medicine-item">
                        <div>
                            <strong>Paracetamol 500mg</strong>
                            <br><small>Strip of 10 tablets</small>
                        </div>
                        <div>
                            <span class="status available">Available</span>
                            <strong>₹15</strong>
                        </div>
                    </div>
                    
                    <button class="btn">🛒 Order from this store</button>
                </div>
            </div>

            <div class="delivery-tracking" id="deliveryTracking" style="display: none;">
                <h3>📦 Order Tracking</h3>
                <p>Order ID: #RH2024001</p>
                
                <div class="tracking-step completed">
                    <div class="step-icon completed">✓</div>
                    <div>
                        <strong>Order Confirmed</strong>
                        <br><small>10:30 AM - Pharmacy received your order</small>
                    </div>
                </div>
                
                <div class="tracking-step completed">
                    <div class="step-icon completed">✓</div>
                    <div>
                        <strong>Order Prepared</strong>
                        <br><small>11:15 AM - Medicines packed and ready</small>
                    </div>
                </div>
                
                <div class="tracking-step active">
                    <div class="step-icon active">🚚</div>
                    <div>
                        <strong>Out for Delivery</strong>
                        <br><small>11:45 AM - Delivery partner on the way</small>
                    </div>
                </div>
                
                <div class="tracking-step">
                    <div class="step-icon pending">📦</div>
                    <div>
                        <strong>Delivered</strong>
                        <br><small>Expected by 12:30 PM</small>
                    </div>
                </div>
            </div>
        </div>

        <!-- Health Records Section -->
        <div id="records" class="content-section">
            <h2>📋 Digital Health Records</h2>
            <p>Secure, QR-verified, paperless prescriptions and certificates</p>

            <div class="form-grid">
                <div>
                    <h3>📤 Upload Document</h3>
                    <div class="qr-scanner">
                        <h4>📱 Scan QR Code or Upload Document</h4>
                        <p>Scan prescription QR codes or upload medical documents</p>
                        <input type="file" id="documentUpload" accept="image/*,application/pdf" style="margin: 10px 0;">
                        <br>
                        <button class="btn">📱 Scan QR Code</button>
                        <button class="btn btn-secondary" onclick="uploadDocument()">📤 Upload Document</button>
                    </div>
                </div>
                <div>
                    <h3>🔍 Search Records</h3>
                    <div class="form-group">
                        <input type="text" id="recordSearch" placeholder="Search by date, doctor, or condition...">
                    </div>
                    <div class="form-group">
                        <label>Date Range</label>
                        <input type="date" id="startDate">
                        <input type="date" id="endDate">
                    </div>
                    <button class="btn">🔍 Search Records</button>
                </div>
            </div>

            <div class="records-display">
                <h3>📋 Your Health Records</h3>
                
                <div class="card">
                    <h4>🏥 Consultation - Dr. Priya Sharma</h4>
                    <p><strong>Date:</strong> 15 Sep 2025</p>
                    <p><strong>Diagnosis:</strong> Viral Fever</p>
                    <p><strong>Prescription:</strong> Paracetamol 500mg - 3 times daily</p>
                    <p><strong>Follow-up:</strong> 3 days</p>
                    <button class="btn">📱 Generate QR</button>
                    <button class="btn btn-secondary">📥 Download</button>
                </div>
                
                <div class="card">
                    <h4>🧪 Lab Report - Blood Test</h4>
                    <p><strong>Date:</strong> 12 Sep 2025</p>
                    <p><strong>Lab:</strong> Rural Health Lab</p>
                    <p><strong>Results:</strong> Normal ranges</p>
                    <button class="btn">📱 Generate QR</button>
                    <button class="btn btn-secondary">📥 Download</button>
                </div>
                
                <div class="card">
                    <h4>💉 Vaccination Record</h4>
                    <p><strong>Date:</strong> 10 Sep 2025</p>
                    <p><strong>Vaccine:</strong> COVID-19 Booster</p>
                    <p><strong>Batch:</strong> COV2024-001</p>
                    <button class="btn">📱 Generate QR</button>
                    <button class="btn btn-secondary">📥 Download</button>
                </div>
            </div>
        </div>

        <!-- Emergency Section -->
        <div id="emergency" class="content-section">
            <div class="emergency-banner">
                🚨 EMERGENCY SERVICES - Call 108 for immediate ambulance
            </div>
            
            <h2>🚨 Emergency Medical Services</h2>
            
            <div class="form-grid">
                <div>
                    <h3>🚨 Report Emergency</h3>
                    <div class="form-group">
                        <label>Emergency Type</label>
                        <select id="emergencyType">
                            <option value="cardiac">Heart Attack / Cardiac</option>
                            <option value="stroke">Stroke</option>
                            <option value="breathing">Breathing Difficulty</option>
                            <option value="accident">Accident / Injury</option>
                            <option value="poisoning">Poisoning</option>
                            <option value="seizure">Seizure</option>
                            <option value="other">Other Emergency</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Current Location</label>
                        <input type="text" id="emergencyLocation" placeholder="Village/Area name">
                        <button class="btn btn-secondary" onclick="getLocation()">📍 Use GPS</button>
                    </div>
                    <div class="form-group">
                        <label>Contact Number</label>
                        <input type="tel" id="emergencyContact" placeholder="Your phone number">
                    </div>
                    <button class="btn btn-danger" onclick="reportEmergency()">🚨 SEND EMERGENCY ALERT</button>
                </div>
                <div>
                    <h3>📞 Emergency Contacts</h3>
                    <div class="card">
                        <h4>🚑 Ambulance</h4>
                        <p><strong>108</strong> - National Ambulance Service</p>
                        <button class="btn btn-danger">📞 Call Now</button>
                    </div>
                    <div class="card">
                        <h4>🏥 Nearest Hospital</h4>
                        <p><strong>Rural District Hospital</strong></p>
                        <p>📍 15 km away</p>
                        <p>📞 +91 12345 67890</p>
                        <button class="btn">📞 Call Hospital</button>
                    </div>
                    <div class="card">
                        <h4>👮 Police</h4>
                        <p><strong>100</strong> - Emergency Police</p>
                        <button class="btn">📞 Call Police</button>
                    </div>
                </div>
            </div>

            <div class="card">
                <h3>🩺 Emergency First Aid</h3>
                <p><strong>For Heart Attack:</strong> Call 108, give aspirin if available, keep patient calm and seated</p>
                <p>
