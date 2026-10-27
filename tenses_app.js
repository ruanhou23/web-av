/**
 * Tenses & 360 Irregular Verbs Interactive Learning & Quiz Module
 * Kết hợp 12 thì trong tiếng Anh và 360 Động từ bất quy tắc
 */

(function () {
  'use strict';

  // 1. Auxiliary & Conjugation Helpers
  function cleanForm(form) {
    if (!form) return '';
    return form.split('/')[0].trim();
  }

  function getVerbSEs(v1) {
    v1 = v1.toLowerCase().trim();
    if (v1 === 'be') return 'is';
    if (v1 === 'have') return 'has';
    if (v1 === 'do') return 'does';
    if (v1 === 'go') return 'goes';
    if (v1.endsWith('ss') || v1.endsWith('sh') || v1.endsWith('ch') || v1.endsWith('x') || v1.endsWith('z') || v1.endsWith('o') || v1.endsWith('s')) {
      return v1 + 'es';
    }
    if (v1.endsWith('y') && v1.length > 1 && !'aeiou'.includes(v1[v1.length - 2])) {
      return v1.slice(0, -1) + 'ies';
    }
    return v1 + 's';
  }

  function getVerbIng(v1) {
    v1 = v1.toLowerCase().trim();
    if (v1 === 'be') return 'being';
    if (v1 === 'see') return 'seeing';
    if (v1.endsWith('ie')) return v1.slice(0, -2) + 'ying';
    if (v1.endsWith('ee') || v1.endsWith('oe') || v1.endsWith('ye')) return v1 + 'ing';

    const vowels = 'aeiou';
    const len = v1.length;
    // CVC doubling for short verbs
    if (len >= 3) {
      const c1 = v1[len - 3];
      const v = v1[len - 2];
      const c2 = v1[len - 1];
      if (!vowels.includes(c1) && vowels.includes(v) && !vowels.includes(c2) && !'wxy'.includes(c2)) {
        if (len <= 4 || ['begin', 'forget', 'prefer', 'permit', 'commit'].includes(v1)) {
          return v1 + c2 + 'ing';
        }
      }
    }
    if (v1.endsWith('e') && !v1.endsWith('ee')) {
      return v1.slice(0, -1) + 'ing';
    }
    return v1 + 'ing';
  }

  // Speak helper using Web Speech API
  function speak(text) {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = (document.getElementById('accent-select')?.value) || 'en-US';
    u.rate = 0.95;
    window.speechSynthesis.speak(u);
  }

  // 2. 12 Tenses Core Knowledge Base
  const TENSES_DATA = [
    // --- GROUP 1: PRESENT TENSES ---
    {
      id: 'present_simple',
      group: 'present',
      groupVi: 'Hiện tại',
      name: 'Present Simple',
      nameVi: 'Hiện tại đơn',
      roleBadge: '⚡ Dùng V1 / V(s,es)',
      badgeColor: 'bg-blue-100 text-blue-800 dark:bg-blue-900/60 dark:text-blue-300',
      gradient: 'from-blue-600 to-cyan-600',
      formula: {
        pos: 'S + V1 / V(s/es) + O',
        neg: 'S + do/does not + V1 + O',
        que: 'Do/Does + S + V1 + O?'
      },
      signals: ['always', 'usually', 'often', 'every day', 'sometimes', 'seldom', 'never'],
      usage: 'Diễn tả thói quen, chân lý hiển nhiên hoặc lịch trình cố định.',
      generateSentences: (v) => {
        const v1 = cleanForm(v.v1);
        const ses = getVerbSEs(v1);
        return {
          pos: `She <span class="text-blue-600 dark:text-blue-400 font-bold">${ses}</span> every morning.`,
          posPlain: `She ${ses} every morning.`,
          neg: `She <span class="text-rose-500 font-bold">does not ${v1}</span> every morning.`,
          que: `<span class="text-indigo-500 font-bold">Does</span> she <span class="font-bold">${v1}</span> every morning?`,
          vi: `Cô ấy ${v.meaning.split(',')[0]} mỗi buổi sáng.`
        };
      }
    },
    {
      id: 'present_continuous',
      group: 'present',
      groupVi: 'Hiện tại',
      name: 'Present Continuous',
      nameVi: 'Hiện tại tiếp diễn',
      roleBadge: '🔄 Dùng am/is/are + V-ing',
      badgeColor: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/60 dark:text-emerald-300',
      gradient: 'from-emerald-600 to-teal-600',
      formula: {
        pos: 'S + am/is/are + V-ing + O',
        neg: 'S + am/is/are not + V-ing + O',
        que: 'Am/Is/Are + S + V-ing + O?'
      },
      signals: ['now', 'right now', 'at the moment', 'currently', 'Look!', 'Listen!'],
      usage: 'Diễn tả hành động đang xảy ra ngay tại thời điểm nói.',
      generateSentences: (v) => {
        const vIng = getVerbIng(cleanForm(v.v1));
        return {
          pos: `They <span class="text-emerald-600 dark:text-emerald-400 font-bold">are ${vIng}</span> right now.`,
          posPlain: `They are ${vIng} right now.`,
          neg: `They <span class="text-rose-500 font-bold">are not ${vIng}</span> right now.`,
          que: `<span class="text-indigo-500 font-bold">Are</span> they <span class="font-bold">${vIng}</span> right now?`,
          vi: `Họ đang ${v.meaning.split(',')[0]} ngay lúc này.`
        };
      }
    },
    {
      id: 'present_perfect',
      group: 'present',
      groupVi: 'Hiện tại',
      name: 'Present Perfect',
      nameVi: 'Hiện tại hoàn thành',
      roleBadge: '🌟 BẮT BUỘC DÙNG V3 (Past Participle)',
      badgeColor: 'bg-amber-100 text-amber-800 dark:bg-amber-900/60 dark:text-amber-300 border border-amber-300/40',
      gradient: 'from-amber-500 to-orange-600',
      formula: {
        pos: 'S + have/has + V3 + O',
        neg: 'S + have/has not + V3 + O',
        que: 'Have/Has + S + V3 + O?'
      },
      signals: ['already', 'yet', 'just', 'ever', 'never', 'since', 'for', 'recently', 'so far'],
      usage: 'Hành động xảy ra trong quá khứ nhưng kết quả hoặc dư âm còn liên quan đến hiện tại.',
      generateSentences: (v) => {
        const v3 = cleanForm(v.v3);
        return {
          pos: `She <span class="text-amber-600 dark:text-amber-400 font-bold">has already ${v3}</span>.`,
          posPlain: `She has already ${v3}.`,
          neg: `She <span class="text-rose-500 font-bold">has not ${v3}</span> yet.`,
          que: `<span class="text-indigo-500 font-bold">Has</span> she <span class="font-bold">${v3}</span> yet?`,
          vi: `Cô ấy đã ${v.meaning.split(',')[0]} rồi.`
        };
      }
    },
    {
      id: 'present_perfect_continuous',
      group: 'present',
      groupVi: 'Hiện tại',
      name: 'Present Perfect Continuous',
      nameVi: 'Hiện tại hoàn thành tiếp diễn',
      roleBadge: '⏱️ have/has been + V-ing',
      badgeColor: 'bg-purple-100 text-purple-800 dark:bg-purple-900/60 dark:text-purple-300',
      gradient: 'from-purple-600 to-indigo-600',
      formula: {
        pos: 'S + have/has been + V-ing + O',
        neg: 'S + have/has not been + V-ing + O',
        que: 'Have/Has + S + been + V-ing + O?'
      },
      signals: ['all day', 'all morning', 'since morning', 'for 3 hours', 'how long'],
      usage: 'Nhấn mạnh tính liên tục kéo dài từ quá khứ đến hiện tại và có thể tiếp tục tương lai.',
      generateSentences: (v) => {
        const vIng = getVerbIng(cleanForm(v.v1));
        return {
          pos: `He <span class="text-purple-600 dark:text-purple-400 font-bold">has been ${vIng}</span> for two hours.`,
          posPlain: `He has been ${vIng} for two hours.`,
          neg: `He <span class="text-rose-500 font-bold">has not been ${vIng}</span> lately.`,
          que: `<span class="text-indigo-500 font-bold">Has</span> he been <span class="font-bold">${vIng}</span> long?`,
          vi: `Anh ấy đã liên tục ${v.meaning.split(',')[0]} suốt 2 tiếng rồi.`
        };
      }
    },

    // --- GROUP 2: PAST TENSES ---
    {
      id: 'past_simple',
      group: 'past',
      groupVi: 'Quá khứ',
      name: 'Past Simple',
      nameVi: 'Quá khứ đơn',
      roleBadge: '⚡ BẮT BUỘC DÙNG V2 (Past Simple)',
      badgeColor: 'bg-rose-100 text-rose-800 dark:bg-rose-900/60 dark:text-rose-300 border border-rose-300/40',
      gradient: 'from-rose-600 to-pink-600',
      formula: {
        pos: 'S + V2 + O',
        neg: 'S + did not + V1 + O',
        que: 'Did + S + V1 + O?'
      },
      signals: ['yesterday', 'ago', 'last night', 'last week', 'in 2020', 'when I was young'],
      usage: 'Diễn tả hành động đã xảy ra và kết thúc hoàn toàn tại một thời điểm xác định trong quá khứ.',
      generateSentences: (v) => {
        const v1 = cleanForm(v.v1);
        const v2 = cleanForm(v.v2);
        return {
          pos: `They <span class="text-rose-600 dark:text-rose-400 font-bold">${v2}</span> yesterday.`,
          posPlain: `They ${v2} yesterday.`,
          neg: `They <span class="text-slate-500 font-bold">did not ${v1}</span> yesterday.`,
          que: `<span class="text-indigo-500 font-bold">Did</span> they <span class="font-bold">${v1}</span> yesterday?`,
          vi: `Họ đã ${v.meaning.split(',')[0]} ngày hôm qua.`
        };
      }
    },
    {
      id: 'past_continuous',
      group: 'past',
      groupVi: 'Quá khứ',
      name: 'Past Continuous',
      nameVi: 'Quá khứ tiếp diễn',
      roleBadge: '🔄 was/were + V-ing',
      badgeColor: 'bg-indigo-100 text-indigo-800 dark:bg-indigo-900/60 dark:text-indigo-300',
      gradient: 'from-indigo-600 to-violet-600',
      formula: {
        pos: 'S + was/were + V-ing + O',
        neg: 'S + was/were not + V-ing + O',
        que: 'Was/Were + S + V-ing + O?'
      },
      signals: ['at 8 PM last night', 'at that time', 'while', 'when', 'all yesterday afternoon'],
      usage: 'Diễn tả hành động đang diễn ra tại một thời điểm hoặc cùng lúc với hành động khác trong quá khứ.',
      generateSentences: (v) => {
        const vIng = getVerbIng(cleanForm(v.v1));
        return {
          pos: `She <span class="text-indigo-600 dark:text-indigo-400 font-bold">was ${vIng}</span> at 8 PM yesterday.`,
          posPlain: `She was ${vIng} at 8 PM yesterday.`,
          neg: `She <span class="text-rose-500 font-bold">was not ${vIng}</span> at that time.`,
          que: `<span class="text-indigo-500 font-bold">Was</span> she <span class="font-bold">${vIng}</span> when you called?`,
          vi: `Cô ấy đang ${v.meaning.split(',')[0]} lúc 8 giờ tối hôm qua.`
        };
      }
    },
    {
      id: 'past_perfect',
      group: 'past',
      groupVi: 'Quá khứ',
      name: 'Past Perfect',
      nameVi: 'Quá khứ hoàn thành',
      roleBadge: '🌟 BẮT BUỘC DÙNG had + V3',
      badgeColor: 'bg-violet-100 text-violet-800 dark:bg-violet-900/60 dark:text-violet-300 border border-violet-300/40',
      gradient: 'from-violet-600 to-purple-700',
      formula: {
        pos: 'S + had + V3 + O',
        neg: 'S + had not + V3 + O',
        que: 'Had + S + V3 + O?'
      },
      signals: ['before', 'after', 'by the time', 'as soon as', 'prior to that'],
      usage: 'Diễn tả một hành động xảy ra và hoàn tất TRƯỚC một hành động khác trong quá khứ.',
      generateSentences: (v) => {
        const v3 = cleanForm(v.v3);
        return {
          pos: `He <span class="text-violet-600 dark:text-violet-400 font-bold">had ${v3}</span> before she arrived.`,
          posPlain: `He had ${v3} before she arrived.`,
          neg: `He <span class="text-rose-500 font-bold">had not ${v3}</span> before the bell rang.`,
          que: `<span class="text-indigo-500 font-bold">Had</span> he <span class="font-bold">${v3}</span> before that?`,
          vi: `Anh ấy đã ${v.meaning.split(',')[0]} trước khi cô ấy đến.`
        };
      }
    },
    {
      id: 'past_perfect_continuous',
      group: 'past',
      groupVi: 'Quá khứ',
      name: 'Past Perfect Continuous',
      nameVi: 'Quá khứ hoàn thành tiếp diễn',
      roleBadge: '⏱️ had been + V-ing',
      badgeColor: 'bg-fuchsia-100 text-fuchsia-800 dark:bg-fuchsia-900/60 dark:text-fuchsia-300',
      gradient: 'from-fuchsia-600 to-pink-600',
      formula: {
        pos: 'S + had been + V-ing + O',
        neg: 'S + had not been + V-ing + O',
        que: 'Had + S + been + V-ing + O?'
      },
      signals: ['before', 'by the time', 'for hours before', 'until then'],
      usage: 'Nhấn mạnh tính liên tục kéo dài của một hành động trước một mốc trong quá khứ.',
      generateSentences: (v) => {
        const vIng = getVerbIng(cleanForm(v.v1));
        return {
          pos: `They <span class="text-fuchsia-600 dark:text-fuchsia-400 font-bold">had been ${vIng}</span> for hours before stopping.`,
          posPlain: `They had been ${vIng} for hours before stopping.`,
          neg: `They <span class="text-rose-500 font-bold">had not been ${vIng}</span> very long.`,
          que: `<span class="text-indigo-500 font-bold">Had</span> they been <span class="font-bold">${vIng}</span> before that?`,
          vi: `Họ đã liên tục ${v.meaning.split(',')[0]} hàng giờ trước khi dừng lại.`
        };
      }
    },

    // --- GROUP 3: FUTURE TENSES ---
    {
      id: 'future_simple',
      group: 'future',
      groupVi: 'Tương lai',
      name: 'Future Simple',
      nameVi: 'Tương lai đơn',
      roleBadge: '⚡ will + V1 (Nguyên thể)',
      badgeColor: 'bg-sky-100 text-sky-800 dark:bg-sky-900/60 dark:text-sky-300',
      gradient: 'from-sky-600 to-blue-600',
      formula: {
        pos: 'S + will + V1 + O',
        neg: 'S + will not (won\'t) + V1 + O',
        que: 'Will + S + V1 + O?'
      },
      signals: ['tomorrow', 'next week', 'in the future', 'soon', 'I think', 'probably'],
      usage: 'Diễn tả quyết định tức thời tại thời điểm nói hoặc dự đoán không có căn cứ chắc chắn.',
      generateSentences: (v) => {
        const v1 = cleanForm(v.v1);
        return {
          pos: `I <span class="text-sky-600 dark:text-sky-400 font-bold">will ${v1}</span> tomorrow.`,
          posPlain: `I will ${v1} tomorrow.`,
          neg: `I <span class="text-rose-500 font-bold">will not ${v1}</span> tomorrow.`,
          que: `<span class="text-indigo-500 font-bold">Will</span> you <span class="font-bold">${v1}</span> tomorrow?`,
          vi: `Tôi sẽ ${v.meaning.split(',')[0]} vào ngày mai.`
        };
      }
    },
    {
      id: 'future_continuous',
      group: 'future',
      groupVi: 'Tương lai',
      name: 'Future Continuous',
      nameVi: 'Tương lai tiếp diễn',
      roleBadge: '🔄 will be + V-ing',
      badgeColor: 'bg-teal-100 text-teal-800 dark:bg-teal-900/60 dark:text-teal-300',
      gradient: 'from-teal-600 to-emerald-600',
      formula: {
        pos: 'S + will be + V-ing + O',
        neg: 'S + will not be + V-ing + O',
        que: 'Will + S + be + V-ing + O?'
      },
      signals: ['at this time tomorrow', 'at 9 AM next Monday', 'this time next week'],
      usage: 'Diễn tả hành động sẽ đang diễn ra tại một thời điểm cụ thể xác định trong tương lai.',
      generateSentences: (v) => {
        const vIng = getVerbIng(cleanForm(v.v1));
        return {
          pos: `She <span class="text-teal-600 dark:text-teal-400 font-bold">will be ${vIng}</span> at this time tomorrow.`,
          posPlain: `She will be ${vIng} at this time tomorrow.`,
          neg: `She <span class="text-rose-500 font-bold">will not be ${vIng}</span> at that time.`,
          que: `<span class="text-indigo-500 font-bold">Will</span> she be <span class="font-bold">${vIng}</span> tomorrow?`,
          vi: `Cô ấy sẽ đang ${v.meaning.split(',')[0]} vào giờ này ngày mai.`
        };
      }
    },
    {
      id: 'future_perfect',
      group: 'future',
      groupVi: 'Tương lai',
      name: 'Future Perfect',
      nameVi: 'Tương lai hoàn thành',
      roleBadge: '🌟 BẮT BUỘC DÙNG will have + V3',
      badgeColor: 'bg-cyan-100 text-cyan-800 dark:bg-cyan-900/60 dark:text-cyan-300 border border-cyan-300/40',
      gradient: 'from-cyan-600 to-blue-700',
      formula: {
        pos: 'S + will have + V3 + O',
        neg: 'S + will not have + V3 + O',
        que: 'Will + S + have + V3 + O?'
      },
      signals: ['by tomorrow', 'by the end of this year', 'by next month', 'before next week'],
      usage: 'Diễn tả hành động sẽ hoàn thành xong TRƯỚC một thời điểm hoặc hành động khác trong tương lai.',
      generateSentences: (v) => {
        const v3 = cleanForm(v.v3);
        return {
          pos: `They <span class="text-cyan-600 dark:text-cyan-400 font-bold">will have ${v3}</span> by next year.`,
          posPlain: `They will have ${v3} by next year.`,
          neg: `They <span class="text-rose-500 font-bold">will not have ${v3}</span> by then.`,
          que: `<span class="text-indigo-500 font-bold">Will</span> they have <span class="font-bold">${v3}</span> by tomorrow?`,
          vi: `Họ sẽ đã ${v.meaning.split(',')[0]} xong trước năm tới.`
        };
      }
    },
    {
      id: 'future_perfect_continuous',
      group: 'future',
      groupVi: 'Tương lai',
      name: 'Future Perfect Continuous',
      nameVi: 'Tương lai hoàn thành tiếp diễn',
      roleBadge: '⏱️ will have been + V-ing',
      badgeColor: 'bg-orange-100 text-orange-800 dark:bg-orange-900/60 dark:text-orange-300',
      gradient: 'from-orange-600 to-amber-600',
      formula: {
        pos: 'S + will have been + V-ing + O',
        neg: 'S + will not have been + V-ing + O',
        que: 'Will + S + have been + V-ing + O?'
      },
      signals: ['by next month... for 5 years', 'by 2030... for a decade'],
      usage: 'Nhấn mạnh khoảng thời gian kéo dài của một hành động tính tới một mốc trong tương lai.',
      generateSentences: (v) => {
        const vIng = getVerbIng(cleanForm(v.v1));
        return {
          pos: `By December, we <span class="text-orange-600 dark:text-orange-400 font-bold">will have been ${vIng}</span> for 5 years.`,
          posPlain: `By December, we will have been ${vIng} for 5 years.`,
          neg: `We <span class="text-rose-500 font-bold">will not have been ${vIng}</span> that long.`,
          que: `<span class="text-indigo-500 font-bold">Will</span> you have been <span class="font-bold">${vIng}</span> for 5 years?`,
          vi: `Tính đến tháng 12, chúng tôi sẽ đã liên tục ${v.meaning.split(',')[0]} được 5 năm.`
        };
      }
    }
  ];

  // 3. Exam / Quiz Question Templates Generator
  const QUIZ_TEMPLATES = [
    {
      type: 'fill_past_simple',
      tenseName: 'Quá khứ đơn (Past Simple)',
      signalWord: 'yesterday / last week / ago',
      explanation: 'Dấu hiệu thời gian trong quá khứ xác định, câu khẳng định bắt buộc chia ở dạng **V2 (Past Simple)**.',
      generate: (v) => {
        const v1 = cleanForm(v.v1);
        const v2 = cleanForm(v.v2);
        const v3 = cleanForm(v.v3);
        const vIng = getVerbIng(v1);
        const prompt = `Yesterday, he ________ (${v1}) to his manager about the project proposal.`;
        return {
          prompt,
          verb: v,
          tenseName: 'Quá khứ đơn (Past Simple)',
          rule: `Động từ bất quy tắc "${v1}" có dạng quá khứ V2 là "${v2}".`,
          correctAnswer: v2,
          options: [v2, v1, v3, `was ${vIng}`].sort(() => Math.random() - 0.5)
        };
      }
    },
    {
      type: 'fill_present_perfect',
      tenseName: 'Hiện tại hoàn thành (Present Perfect)',
      signalWord: 'already / since / recently',
      explanation: 'Dấu hiệu "already" hoặc "since" diễn tả hành động vừa hoàn thành, công thức là **have/has + V3 (Past Participle)**.',
      generate: (v) => {
        const v1 = cleanForm(v.v1);
        const v2 = cleanForm(v.v2);
        const v3 = cleanForm(v.v3);
        const prompt = `She has already ________ (${v1}) all the required documents.`;
        return {
          prompt,
          verb: v,
          tenseName: 'Hiện tại hoàn thành (Present Perfect)',
          rule: `Sau trợ động từ "has/have", động từ bất quy tắc bắt buộc chuyển sang dạng quá khứ phân từ V3 là "${v3}".`,
          correctAnswer: v3,
          options: [v3, v2, v1, `${v1}ing`].sort(() => Math.random() - 0.5)
        };
      }
    },
    {
      type: 'fill_past_perfect',
      tenseName: 'Quá khứ hoàn thành (Past Perfect)',
      signalWord: 'before / by the time',
      explanation: 'Hành động xảy ra trước một hành động khác trong quá khứ, dùng **had + V3**.',
      generate: (v) => {
        const v1 = cleanForm(v.v1);
        const v2 = cleanForm(v.v2);
        const v3 = cleanForm(v.v3);
        const prompt = `By the time the manager arrived, the team ________ (${v1}) the entire plan.`;
        return {
          prompt,
          verb: v,
          tenseName: 'Quá khứ hoàn thành (Past Perfect)',
          rule: `Hành động xảy ra trước dùng "had + V3", do đó đáp án là "had ${v3}".`,
          correctAnswer: `had ${v3}`,
          options: [`had ${v3}`, `has ${v3}`, v2, `was ${v1}`].sort(() => Math.random() - 0.5)
        };
      }
    },
    {
      type: 'fill_future_perfect',
      tenseName: 'Tương lai hoàn thành (Future Perfect)',
      signalWord: 'by tomorrow / by the end of this year',
      explanation: 'Diễn tả hành động sẽ hoàn tất trước một thời điểm tương lai, dùng **will have + V3**.',
      generate: (v) => {
        const v1 = cleanForm(v.v1);
        const v3 = cleanForm(v.v3);
        const prompt = `By the end of this month, we ________ (${v1}) our key objectives.`;
        return {
          prompt,
          verb: v,
          tenseName: 'Tương lai hoàn thành (Future Perfect)',
          rule: `Công thức: "will have + V3", dạng V3 của "${v1}" là "${v3}".`,
          correctAnswer: `will have ${v3}`,
          options: [`will have ${v3}`, `will ${v1}`, `have ${v3}`, `will be ${v1}`].sort(() => Math.random() - 0.5)
        };
      }
    },
    {
      type: 'fill_present_continuous',
      tenseName: 'Hiện tại tiếp diễn (Present Continuous)',
      signalWord: 'Listen! / right now / at the moment',
      explanation: 'Hành động đang diễn ra tại thời điểm nói, dùng **am/is/are + V-ing**.',
      generate: (v) => {
        const v1 = cleanForm(v.v1);
        const v2 = cleanForm(v.v2);
        const vIng = getVerbIng(v1);
        const prompt = `Listen! Someone ________ (${v1}) outside the conference room.`;
        return {
          prompt,
          verb: v,
          tenseName: 'Hiện tại tiếp diễn (Present Continuous)',
          rule: `Chủ ngữ "Someone" số ít đi kèm "is + V-ing", dạng V-ing của "${v1}" là "${vIng}".`,
          correctAnswer: `is ${vIng}`,
          options: [`is ${vIng}`, `are ${vIng}`, v2, v1].sort(() => Math.random() - 0.5)
        };
      }
    },
    {
      type: 'fill_past_continuous',
      tenseName: 'Quá khứ tiếp diễn (Past Continuous)',
      signalWord: 'while / at 8 PM yesterday',
      explanation: 'Một hành động đang diễn ra thì một hành động ngắn khác xen vào (hành động đang diễn ra dùng was/were + V-ing, hành động xen vào dùng V2).',
      generate: (v) => {
        const v1 = cleanForm(v.v1);
        const v2 = cleanForm(v.v2);
        const vIng = getVerbIng(v1);
        const prompt = `While they were working in the office, the lights suddenly ________ (${v1}).`;
        return {
          prompt,
          verb: v,
          tenseName: 'Quá khứ đơn xen vào quá khứ tiếp diễn',
          rule: `Hành động bất ngờ xen vào chia ở quá khứ đơn V2, dạng V2 của "${v1}" là "${v2}".`,
          correctAnswer: v2,
          options: [v2, `were ${vIng}`, `had ${cleanForm(v.v3)}`, v1].sort(() => Math.random() - 0.5)
        };
      }
    }
  ];

  // 4. Module State
  const TensesState = {
    verbs: [],
    selectedVerb: null,
    activeGroupFilter: 'all', // all, present, past, future, perfect, simple
    activeSubView: 'visual', // visual, quiz
    
    // Quiz State
    quizQuestions: [],
    quizIndex: 0,
    quizScore: 0,
    quizStreak: 0,
    quizAnswered: false,
    quizTotal: 10
  };

  // 5. Main App Object
  const TensesApp = {
    initialized: false,

    init() {
      TensesState.verbs = window.IRREGULAR_VERBS || [];
      if (!TensesState.verbs.length) return;

      if (!TensesState.selectedVerb) {
        // Default to a rich popular verb like 'write' or 'go'
        const defaultVerb = TensesState.verbs.find(v => v.v1 === 'write') || TensesState.verbs[0];
        TensesState.selectedVerb = defaultVerb;
      }

      if (!this.initialized) {
        this.setupEventListeners();
        this.renderPopularShortcuts();
        this.initialized = true;
      }

      this.renderVisualConjugator();
    },

    setupEventListeners() {
      // Sub-view toggle (Visual Lessons vs Quiz)
      const visualBtn = document.getElementById('tenses-subview-visual-btn');
      const quizBtn = document.getElementById('tenses-subview-quiz-btn');

      if (visualBtn) {
        visualBtn.addEventListener('click', () => {
          this.switchSubView('visual');
        });
      }
      if (quizBtn) {
        quizBtn.addEventListener('click', () => {
          this.switchSubView('quiz');
        });
      }

      // Verb search input for 12 tenses
      const searchInput = document.getElementById('tenses-verb-search');
      const searchResults = document.getElementById('tenses-search-results');

      if (searchInput && searchResults) {
        searchInput.addEventListener('input', (e) => {
          const q = e.target.value.toLowerCase().trim();
          if (!q) {
            searchResults.classList.add('hidden');
            return;
          }

          const matches = TensesState.verbs.filter(v =>
            v.v1.toLowerCase().includes(q) ||
            v.v2.toLowerCase().includes(q) ||
            v.v3.toLowerCase().includes(q) ||
            v.meaning.toLowerCase().includes(q)
          ).slice(0, 8);

          if (matches.length > 0) {
            searchResults.innerHTML = matches.map(v => `
              <div class="px-4 py-2.5 hover:bg-indigo-50 dark:hover:bg-slate-700 cursor-pointer flex items-center justify-between border-b border-slate-100 dark:border-slate-700 text-xs sm:text-sm" data-verb-id="${v.id}">
                <div class="flex items-center space-x-2">
                  <span class="text-base">${v.icon || '📖'}</span>
                  <span class="font-bold text-slate-800 dark:text-white">${v.v1}</span>
                  <span class="text-slate-400">→</span>
                  <span class="text-indigo-600 dark:text-indigo-400 font-semibold">${v.v2}</span>
                  <span class="text-slate-400">→</span>
                  <span class="text-emerald-600 dark:text-emerald-400 font-semibold">${v.v3}</span>
                </div>
                <span class="text-slate-500 dark:text-slate-400 text-xs italic">${v.meaning.split(',')[0]}</span>
              </div>
            `).join('');
            searchResults.classList.remove('hidden');

            searchResults.querySelectorAll('[data-verb-id]').forEach(el => {
              el.addEventListener('click', () => {
                const vid = parseInt(el.dataset.verbId);
                const targetVerb = TensesState.verbs.find(v => v.id === vid);
                if (targetVerb) {
                  this.selectVerb(targetVerb);
                  searchInput.value = '';
                  searchResults.classList.add('hidden');
                }
              });
            });
          } else {
            searchResults.innerHTML = `<div class="p-3 text-xs text-slate-400 text-center">Không tìm thấy động từ phù hợp</div>`;
            searchResults.classList.remove('hidden');
          }
        });

        // Hide search dropdown on click outside
        document.addEventListener('click', (e) => {
          if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.classList.add('hidden');
          }
        });
      }

      // Group Filters (All, Present, Past, Future, Perfect, Simple)
      document.querySelectorAll('[data-tense-group]').forEach(btn => {
        btn.addEventListener('click', () => {
          document.querySelectorAll('[data-tense-group]').forEach(b => {
            b.classList.remove('bg-indigo-600', 'text-white', 'shadow-md');
            b.classList.add('bg-slate-100', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');
          });
          btn.classList.add('bg-indigo-600', 'text-white', 'shadow-md');
          btn.classList.remove('bg-slate-100', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');

          TensesState.activeGroupFilter = btn.dataset.tenseGroup;
          this.renderTenseCards();
        });
      });

      // Random Verb Button
      const randBtn = document.getElementById('tenses-random-verb-btn');
      if (randBtn) {
        randBtn.addEventListener('click', () => {
          const rand = TensesState.verbs[Math.floor(Math.random() * TensesState.verbs.length)];
          this.selectVerb(rand);
        });
      }
    },

    switchSubView(view) {
      TensesState.activeSubView = view;
      const visualBtn = document.getElementById('tenses-subview-visual-btn');
      const quizBtn = document.getElementById('tenses-subview-quiz-btn');
      const visualWrapper = document.getElementById('tenses-visual-wrapper');
      const quizWrapper = document.getElementById('tenses-quiz-wrapper');

      if (visualBtn && quizBtn) {
        if (view === 'visual') {
          visualBtn.classList.add('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-indigo-600', 'dark:text-indigo-400');
          visualBtn.classList.remove('text-slate-600', 'dark:text-slate-400');
          quizBtn.classList.remove('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-indigo-600', 'dark:text-indigo-400');
          quizBtn.classList.add('text-slate-600', 'dark:text-slate-400');
        } else {
          quizBtn.classList.add('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-indigo-600', 'dark:text-indigo-400');
          quizBtn.classList.remove('text-slate-600', 'dark:text-slate-400');
          visualBtn.classList.remove('bg-white', 'dark:bg-slate-700', 'shadow-sm', 'text-indigo-600', 'dark:text-indigo-400');
          visualBtn.classList.add('text-slate-600', 'dark:text-slate-400');
        }
      }

      const subVisualBtn = document.getElementById('subnav-tenses-visual-btn');
      const subQuizBtn = document.getElementById('subnav-tenses-quiz-btn');
      if (subVisualBtn && subQuizBtn) {
        if (view === 'visual') {
          subVisualBtn.className = 'sub-tab-btn px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-100 dark:bg-amber-900/60 text-amber-700 dark:text-amber-300 border border-amber-200 dark:border-amber-800/80 shadow-2xs flex items-center gap-1.5';
          subQuizBtn.className = 'sub-tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-white dark:hover:bg-slate-800 transition-all flex items-center gap-1.5';
        } else {
          subQuizBtn.className = 'sub-tab-btn px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-100 dark:bg-amber-900/60 text-amber-700 dark:text-amber-300 border border-amber-200 dark:border-amber-800/80 shadow-2xs flex items-center gap-1.5';
          subVisualBtn.className = 'sub-tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-white dark:hover:bg-slate-800 transition-all flex items-center gap-1.5';
        }
      }

      if (visualWrapper) visualWrapper.classList.toggle('hidden', view !== 'visual');
      if (quizWrapper) quizWrapper.classList.toggle('hidden', view !== 'quiz');

      if (view === 'visual') {
        this.renderVisualConjugator();
      } else {
        this.startQuiz();
      }
    },

    selectVerb(verb) {
      TensesState.selectedVerb = verb;
      this.renderVisualConjugator();
    },

    renderPopularShortcuts() {
      const container = document.getElementById('tenses-popular-shortcuts');
      if (!container) return;

      const popularList = ['write', 'go', 'see', 'take', 'break', 'make', 'come', 'give', 'know', 'eat', 'build', 'speak'];
      const matched = popularList.map(w => TensesState.verbs.find(v => v.v1 === w)).filter(Boolean);

      container.innerHTML = matched.map(v => `
        <button class="px-3 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center space-x-1.5 border border-slate-200/80 dark:border-slate-700 hover:border-indigo-400 bg-white dark:bg-slate-800 hover:bg-indigo-50 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 btn-press" data-shortcut-id="${v.id}">
          <span>${v.icon || '⚡'}</span>
          <span>${v.v1}</span>
        </button>
      `).join('');

      container.querySelectorAll('[data-shortcut-id]').forEach(btn => {
        btn.addEventListener('click', () => {
          const vid = parseInt(btn.dataset.shortcutId);
          const v = TensesState.verbs.find(item => item.id === vid);
          if (v) this.selectVerb(v);
        });
      });
    },

    renderVisualConjugator() {
      const v = TensesState.selectedVerb;
      if (!v) return;

      const v1 = cleanForm(v.v1);
      const v2 = cleanForm(v.v2);
      const v3 = cleanForm(v.v3);
      const vIng = getVerbIng(v1);
      const vSes = getVerbSEs(v1);

      // Hero Selected Verb Banner
      const iconEl = document.getElementById('tenses-hero-icon');
      const titleEl = document.getElementById('tenses-hero-title');
      const ipaEl = document.getElementById('tenses-hero-ipa');
      const meaningEl = document.getElementById('tenses-hero-meaning');
      const v1El = document.getElementById('tenses-hero-v1');
      const v2El = document.getElementById('tenses-hero-v2');
      const v3El = document.getElementById('tenses-hero-v3');
      const vIngEl = document.getElementById('tenses-hero-ving');
      const vSesEl = document.getElementById('tenses-hero-vses');

      if (iconEl) iconEl.textContent = v.icon || '🌟';
      if (titleEl) titleEl.textContent = v.v1.toUpperCase();
      if (ipaEl) ipaEl.textContent = v.ipa;
      if (meaningEl) meaningEl.textContent = v.meaning;

      if (v1El) v1El.textContent = v1;
      if (v2El) v2El.textContent = v2;
      if (v3El) v3El.textContent = v3;
      if (vIngEl) vIngEl.textContent = vIng;
      if (vSesEl) vSesEl.textContent = vSes;

      // Audio speaks for hero forms
      document.querySelectorAll('[data-tense-speak]').forEach(btn => {
        btn.onclick = (e) => {
          e.stopPropagation();
          const target = btn.dataset.tenseSpeak;
          if (target === 'v1') speak(v1);
          else if (target === 'v2') speak(v2);
          else if (target === 'v3') speak(v3);
          else if (target === 'ving') speak(vIng);
        };
      });

      this.renderTenseCards();
    },

    renderTenseCards() {
      const container = document.getElementById('tenses-cards-grid');
      if (!container) return;

      const v = TensesState.selectedVerb;
      if (!v) return;

      const filter = TensesState.activeGroupFilter;
      const list = TENSES_DATA.filter(t => {
        if (filter === 'all') return true;
        if (filter === 'present' && t.group === 'present') return true;
        if (filter === 'past' && t.group === 'past') return true;
        if (filter === 'future' && t.group === 'future') return true;
        if (filter === 'perfect' && (t.id.includes('perfect') && !t.id.includes('continuous'))) return true;
        if (filter === 'continuous' && t.id.includes('continuous')) return true;
        if (filter === 'simple' && t.id.includes('simple')) return true;
        return false;
      });

      container.innerHTML = list.map((t, idx) => {
        const sentences = t.generateSentences(v);
        return `
          <div class="bg-white dark:bg-slate-800/90 rounded-3xl p-5 sm:p-6 border border-slate-200/80 dark:border-slate-700/80 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between space-y-4 group">
            
            <!-- Card Header -->
            <div>
              <div class="flex items-center justify-between gap-2 mb-2">
                <span class="px-2.5 py-1 rounded-lg text-[10px] sm:text-xs font-bold uppercase tracking-wider ${t.badgeColor}">
                  ${t.groupVi}
                </span>
                <span class="text-xs font-bold text-slate-400">#${idx + 1}</span>
              </div>

              <h3 class="text-xl font-black text-slate-900 dark:text-white flex items-center justify-between">
                <span>${t.name}</span>
              </h3>
              <p class="text-xs font-semibold text-indigo-600 dark:text-indigo-400 mt-0.5">${t.nameVi}</p>
              
              <!-- Role Badge (V1, V2, V3 requirement) -->
              <div class="mt-2.5 inline-flex items-center px-2.5 py-1 rounded-md text-xs font-bold bg-slate-100 dark:bg-slate-700/70 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-600">
                ${t.roleBadge}
              </div>
            </div>

            <!-- Formulas Box -->
            <div class="bg-slate-50 dark:bg-slate-900/60 p-3.5 rounded-2xl border border-slate-200/60 dark:border-slate-700/60 space-y-1.5 text-xs">
              <div class="font-bold text-slate-400 uppercase text-[10px] tracking-wider mb-1">Công thức:</div>
              <div class="flex items-start space-x-2 font-mono text-slate-700 dark:text-slate-300">
                <span class="w-4 text-emerald-600 font-bold">(+)</span>
                <span class="font-medium">${t.formula.pos}</span>
              </div>
              <div class="flex items-start space-x-2 font-mono text-slate-700 dark:text-slate-300">
                <span class="w-4 text-rose-500 font-bold">(-)</span>
                <span class="font-medium">${t.formula.neg}</span>
              </div>
              <div class="flex items-start space-x-2 font-mono text-slate-700 dark:text-slate-300">
                <span class="w-4 text-indigo-500 font-bold">(?)</span>
                <span class="font-medium">${t.formula.que}</span>
              </div>
            </div>

            <!-- Signal Words -->
            <div>
              <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400 mb-1.5">Dấu hiệu nhận biết:</div>
              <div class="flex flex-wrap gap-1.5">
                ${t.signals.map(s => `<span class="px-2 py-0.5 rounded-md text-[11px] font-semibold bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-300 border border-indigo-200/50 dark:border-indigo-800/50">${s}</span>`).join('')}
              </div>
            </div>

            <!-- Example Sentence with Active Verb -->
            <div class="bg-gradient-to-r from-blue-50/70 to-indigo-50/70 dark:from-slate-900/80 dark:to-indigo-950/40 p-4 rounded-2xl border border-blue-100 dark:border-indigo-900/50 space-y-2">
              <div class="flex items-start justify-between gap-2">
                <div class="text-sm font-semibold text-slate-800 dark:text-slate-100 leading-relaxed">
                  "${sentences.pos}"
                </div>
                <button class="w-8 h-8 rounded-full bg-white dark:bg-slate-800 shadow-sm hover:bg-blue-600 hover:text-white dark:hover:bg-indigo-600 text-slate-600 dark:text-slate-300 flex items-center justify-center transition-all flex-shrink-0 btn-press" data-speak-sentence="${sentences.posPlain}" title="Phát âm câu này">
                  <i class="fa-solid fa-volume-high text-xs"></i>
                </button>
              </div>
              <p class="text-xs text-slate-500 dark:text-slate-400 italic">
                👉 ${sentences.vi}
              </p>
            </div>

          </div>
        `;
      }).join('');

      // Attach audio buttons
      container.querySelectorAll('[data-speak-sentence]').forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.stopPropagation();
          speak(btn.dataset.speakSentence);
        });
      });
    },

    // 6. Exam / Quiz Engine
    startQuiz() {
      TensesState.quizScore = 0;
      TensesState.quizStreak = 0;
      TensesState.quizIndex = 0;
      TensesState.quizAnswered = false;

      // Generate 10 randomized dynamic questions
      const poolVerbs = [...TensesState.verbs].sort(() => Math.random() - 0.5);
      const questions = [];

      for (let i = 0; i < TensesState.quizTotal; i++) {
        const verb = poolVerbs[i % poolVerbs.length];
        const tmpl = QUIZ_TEMPLATES[Math.floor(Math.random() * QUIZ_TEMPLATES.length)];
        questions.push(tmpl.generate(verb));
      }

      TensesState.quizQuestions = questions;

      const activeCard = document.getElementById('tenses-quiz-active-card');
      const resultCard = document.getElementById('tenses-quiz-result-card');
      if (activeCard) activeCard.classList.remove('hidden');
      if (resultCard) resultCard.classList.add('hidden');

      this.renderQuizQuestion();
    },

    renderQuizQuestion() {
      const q = TensesState.quizQuestions[TensesState.quizIndex];
      if (!q) {
        this.finishQuiz();
        return;
      }

      TensesState.quizAnswered = false;

      const progressEl = document.getElementById('tenses-quiz-progress-text');
      const scoreEl = document.getElementById('tenses-quiz-score');
      const streakEl = document.getElementById('tenses-quiz-streak');
      const barEl = document.getElementById('tenses-quiz-bar');
      const promptEl = document.getElementById('tenses-quiz-prompt');
      const tenseBadgeEl = document.getElementById('tenses-quiz-tense-badge');
      const optionsBox = document.getElementById('tenses-quiz-options-container');
      const explBox = document.getElementById('tenses-quiz-explanation');

      if (progressEl) progressEl.textContent = `Câu ${TensesState.quizIndex + 1} / ${TensesState.quizTotal}`;
      if (scoreEl) scoreEl.textContent = `Điểm: ${TensesState.quizScore}`;
      if (streakEl) streakEl.innerHTML = `<i class="fa-solid fa-fire text-amber-500 mr-1"></i>Streak: ${TensesState.quizStreak}`;
      if (barEl) barEl.style.width = `${((TensesState.quizIndex + 1) / TensesState.quizTotal) * 100}%`;
      if (promptEl) promptEl.textContent = q.prompt;
      if (tenseBadgeEl) tenseBadgeEl.textContent = q.tenseName;
      if (explBox) explBox.classList.add('hidden');

      if (optionsBox) {
        optionsBox.innerHTML = q.options.map((opt, idx) => `
          <button class="tenses-quiz-opt w-full p-4 rounded-2xl border-2 border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-left font-bold text-slate-800 dark:text-slate-100 hover:border-indigo-500 hover:bg-indigo-50/50 dark:hover:bg-slate-700/60 transition-all flex items-center justify-between group btn-press" data-opt-idx="${idx}" data-val="${opt}">
            <div class="flex items-center space-x-3">
              <span class="w-8 h-8 rounded-xl bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 font-bold flex items-center justify-center text-xs group-hover:bg-indigo-600 group-hover:text-white transition-colors">
                ${String.fromCharCode(65 + idx)}
              </span>
              <span class="text-base">${opt}</span>
            </div>
            <span class="tenses-opt-icon opacity-0"></span>
          </button>
        `).join('');

        optionsBox.querySelectorAll('.tenses-quiz-opt').forEach(btn => {
          btn.addEventListener('click', () => this.handleQuizAnswer(btn.dataset.val, btn));
        });
      }
    },

    handleQuizAnswer(selectedVal, clickedBtn) {
      if (TensesState.quizAnswered) return;
      TensesState.quizAnswered = true;

      const q = TensesState.quizQuestions[TensesState.quizIndex];
      const isCorrect = (selectedVal === q.correctAnswer);

      if (isCorrect) {
        TensesState.quizScore += 10;
        TensesState.quizStreak += 1;
        clickedBtn.classList.remove('border-slate-200', 'dark:border-slate-700');
        clickedBtn.classList.add('border-emerald-500', 'bg-emerald-50', 'dark:bg-emerald-950/60', 'text-emerald-700', 'dark:text-emerald-300');
        const icon = clickedBtn.querySelector('.tenses-opt-icon');
        if (icon) icon.innerHTML = '<i class="fa-solid fa-circle-check text-emerald-500 text-xl opacity-100"></i>';
      } else {
        TensesState.quizStreak = 0;
        clickedBtn.classList.remove('border-slate-200', 'dark:border-slate-700');
        clickedBtn.classList.add('border-rose-500', 'bg-rose-50', 'dark:bg-rose-950/60', 'text-rose-700', 'dark:text-rose-300');
        const icon = clickedBtn.querySelector('.tenses-opt-icon');
        if (icon) icon.innerHTML = '<i class="fa-solid fa-circle-xmark text-rose-500 text-xl opacity-100"></i>';

        // Highlight the correct one
        document.querySelectorAll('.tenses-quiz-opt').forEach(b => {
          if (b.dataset.val === q.correctAnswer) {
            b.classList.remove('border-slate-200', 'dark:border-slate-700');
            b.classList.add('border-emerald-500', 'bg-emerald-50', 'dark:bg-emerald-950/60', 'text-emerald-700', 'dark:text-emerald-300');
            const cIcon = b.querySelector('.tenses-opt-icon');
            if (cIcon) cIcon.innerHTML = '<i class="fa-solid fa-circle-check text-emerald-500 text-xl opacity-100"></i>';
          }
        });
      }

      // Show detailed explanation box
      const explBox = document.getElementById('tenses-quiz-explanation');
      const explVerdict = document.getElementById('tenses-quiz-expl-verdict');
      const explRule = document.getElementById('tenses-quiz-expl-rule');
      const explNextBtn = document.getElementById('tenses-quiz-next-btn');

      if (explBox) {
        explBox.classList.remove('hidden');
        if (explVerdict) {
          explVerdict.innerHTML = isCorrect
            ? '<span class="text-emerald-600 dark:text-emerald-400 font-extrabold flex items-center gap-1.5"><i class="fa-solid fa-circle-check"></i> Chính xác! (+10 điểm)</span>'
            : `<span class="text-rose-600 dark:text-rose-400 font-extrabold flex items-center gap-1.5"><i class="fa-solid fa-circle-xmark"></i> Chưa đúng! Đáp án đúng: <strong>"${q.correctAnswer}"</strong></span>`;
        }
        if (explRule) {
          explRule.innerHTML = `<strong>Giải thích ngữ pháp:</strong> ${q.rule}`;
        }
        if (explNextBtn) {
          explNextBtn.focus();
          explNextBtn.onclick = () => {
            TensesState.quizIndex++;
            this.renderQuizQuestion();
          };
        }
      }
    },

    finishQuiz() {
      const activeCard = document.getElementById('tenses-quiz-active-card');
      const resultCard = document.getElementById('tenses-quiz-result-card');
      if (activeCard) activeCard.classList.add('hidden');
      if (resultCard) resultCard.classList.remove('hidden');

      const maxScore = TensesState.quizTotal * 10;
      const score = TensesState.quizScore;
      const pct = Math.round((score / maxScore) * 100);

      document.getElementById('tenses-quiz-final-score').textContent = `${score} / ${maxScore}`;
      document.getElementById('tenses-quiz-final-percent').textContent = `${pct}%`;

      let msg = '';
      if (pct === 100) msg = 'Xuất sắc! Bạn đã làm chủ hoàn toàn 12 thì và động từ bất quy tắc! 🔥';
      else if (pct >= 80) msg = 'Rất tốt! Kiến thức chia thì và động từ bất quy tắc của bạn rất vững vàng!';
      else if (pct >= 50) msg = 'Khá ổn! Hãy luyện thêm để phân biệt chính xác giữa V2 và V3 trong các thì hoàn thành nhé!';
      else msg = 'Cần ôn lại thêm bảng 12 thì và dạng V2, V3 của các động từ bất quy tắc!';

      document.getElementById('tenses-quiz-final-message').textContent = msg;

      const restartBtn = document.getElementById('tenses-quiz-restart-btn');
      if (restartBtn) restartBtn.onclick = () => this.startQuiz();
    }
  };

  window.TensesApp = TensesApp;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => TensesApp.init());
  } else {
    TensesApp.init();
  }
})();
