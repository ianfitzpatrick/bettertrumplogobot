import codecs, random

def get_lines(basedir, subdir='corpus/'):
    t_line = codecs.open('%s%st.txt' % (basedir, subdir) ,'r', 'utf-8').read().split('\n')
    p_line = codecs.open('%s%sp.txt' % (basedir, subdir) ,'r', 'utf-8').read().split('\n')
    m_line = codecs.open('%s%sm.txt' % (basedir, subdir),'r', 'utf-8').read().split('\n')

    return ( random.choice(t_line), random.choice(p_line), random.choice(m_line) )
