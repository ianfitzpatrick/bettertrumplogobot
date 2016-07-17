import codecs, random

def get_lines(subdir='corpus/'):
    t_line = codecs.open('%st.txt' % subdir ,'r', 'utf-8').read().split('\n')
    p_line = codecs.open('%sp.txt' % subdir ,'r', 'utf-8').read().split('\n')
    m_line = codecs.open('%sm.txt' % subdir,'r', 'utf-8').read().split('\n')

    return ( random.choice(t_line), random.choice(p_line), random.choice(m_line) )
